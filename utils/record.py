import asyncio
import speech_recognition as sr
from yaspin import yaspin

recognizer = sr.Recognizer()

async def non_blocking_input(prompt, queue):
    await asyncio.get_event_loop().run_in_executor(None, input, prompt)
    await queue.put("stop")

async def capture_audio(timeout, queue):
    with sr.Microphone() as source:
        try:
            with yaspin(text="🎤 Recording...", spinner="dots12") as spinner:
                spinner.start()
                audio = await asyncio.get_event_loop().run_in_executor(None, lambda: recognizer.listen(source, timeout=timeout))
                await queue.put(audio)
        except sr.WaitTimeoutError:
            await queue.put("timeout")

async def record_and_transcribe(timeout=30):
    queue = asyncio.Queue()

    input_coro = non_blocking_input("Press Enter to stop recording: ", queue)
    capture_coro = capture_audio(timeout, queue)

    tasks = [input_coro, capture_coro]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # Cancel any pending tasks
    for task in pending:
        task.cancel()

    # Check if we have something in the queue and get the result
    if not queue.empty():
        result = await queue.get()

        if isinstance(result, sr.AudioData):
            with yaspin(text="💭 Recognizing...", spinner="dots12") as spinner:
                spinner.start()
                try:
                    text = recognizer.recognize_google(result)
                    return text
                except sr.UnknownValueError:
                    print("Could not understand audio")
                    return None
                except sr.RequestError as e:
                    print(f"Error during recognition: {e}")
                    return None
    else:
        print("Recording was not successful.")
        return None