import asyncio
import speech_recognition as sr

# Initialize speech recognition engine
recognizer = sr.Recognizer()

async def record_and_transcribe():
    """
    Call the record function to record the user voice, waits for the
    recording to complete and then perform the recording transcript
    which will be then returned
    """
    loop = asyncio.get_event_loop()

    def capture_audio():
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5)  # Set a timeout (5 seconds in this case)
                return audio
            except sr.WaitTimeoutError:
                print("Recording timed out.")
                return None

    try:
        future = loop.run_in_executor(None, capture_audio)
        user_input_task = loop.run_in_executor(None, input, "Press Enter to stop recording: ")
        done, pending = await asyncio.wait([future, user_input_task], return_when=asyncio.FIRST_COMPLETED)

        # Cancel any pending tasks
        for task in pending:
            task.cancel()

        # Get the result from the completed task
        audio = done.pop().result()

        if audio:
            print("Recognizing...")
            try:
                text = recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error during recognition: {e}")

    except asyncio.CancelledError:
        print("Recording canceled.")

if __name__ == "__main__":
    asyncio.run(record_and_transcribe())
