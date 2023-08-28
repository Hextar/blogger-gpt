import asyncio
import speech_recognition as sr

# Initialize speech recognition engine
recognizer = sr.Recognizer()

# Call the record function to record the user voice, waits for the
# recording to complete and then perform the recording transcript
# which will be then returned
async def record_and_transcribe():
    loop = asyncio.get_event_loop()

    def capture_audio():
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        return audio

    audio = await loop.run_in_executor(None, capture_audio)

    print("Recognizing...")
    try:
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error during recognition: {e}")
