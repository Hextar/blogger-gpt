import asyncio
import speech_recognition as sr
from yaspin import yaspin

async def capture_audio(recognizer, timeout, queue):
    try:
        with sr.Microphone() as source:
            with yaspin(text="🎤 Recording your voice...", color="yellow") as spinner:
                audio = await asyncio.get_event_loop().run_in_executor(None, lambda: recognizer.listen(source, timeout=timeout))
                spinner.text = "Finished recording."
            await queue.put(audio)
    except Exception as e:
        await queue.put("error")

async def record_and_transcribe(timeout=120, energy_threshold=4000 ):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = energy_threshold

    queue = asyncio.Queue()
    capture_coro = capture_audio(recognizer, timeout, queue)
    done, _ = await asyncio.wait([capture_coro], return_when=asyncio.FIRST_COMPLETED, timeout=60)

    if not queue.empty():
        result = await queue.get()
        if isinstance(result, sr.AudioData):
            with yaspin(text="📠 Transcribing...", color="green") as spinner:
                try:
                    text = recognizer.recognize_google(result)
                    spinner.text = "Transcription complete."
                    return text
                except sr.UnknownValueError:
                    return None
                except sr.RequestError as e:
                    return None
        else:
            return None
    else:
        return None
