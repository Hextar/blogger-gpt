from gtts import gTTS
import playsound


def debug_text_to_speech(text):
    tts = gTTS(text)
    output_file = ".temp/debug.mp3"
    tts.save(output_file)

    playsound.playsound(output_file)