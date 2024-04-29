import speech_recognition as sr
import os 
from mp3ToWav import convert_mp3_to_wav  # Fix import statement from the correct module

# Function to recognize speech from audio file
def recognize_speech(file_name):
    # Initialize recognizer class (for recognizing speech)
    r = sr.Recognizer()

    # Get the directory of the current Python script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Full path to the file
    audio_path = os.path.join(script_dir, file_name)

    # Convert MP3 to WAV if needed
    mp3_file = audio_path
    wav_file = os.path.join(script_dir, "1.wav")
    convert_mp3_to_wav(mp3_file, wav_file)

    # Reading the audio file as source
    with sr.AudioFile(wav_file) as source:
        audio_text = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio_text, language='en-US')
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)
