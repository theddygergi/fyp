import speech_recognition as sr

def transcribe_wav(wav_file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Load the WAV file
    with sr.AudioFile(wav_file) as source:
        # Listen for the data (load audio to memory)
        audio_data = recognizer.record(source)
        
        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
