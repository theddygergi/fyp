import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import mediainfo

def recognize_speech_from_mp3(mp3_file):
    recognizer = sr.Recognizer()
    
    try:
        # Load the audio file using PyDub
        audio = AudioSegment.from_file(mp3_file)
        
        # Convert the audio to raw PCM data
        raw_audio_data = audio.raw_data
        sample_rate = audio.frame_rate
        
        # Recognize speech from the raw audio data
        text = recognizer.recognize_google(audio_data=raw_audio_data, sample_rate=sample_rate)
        return text
    except Exception as e:
        print(f"Error recognizing speech: {e}")
        return None

def solve_recaptcha(mp3_file):
    # Recognize speech from the MP3 file
    captcha_text = recognize_speech_from_mp3(mp3_file)
    if captcha_text:
        print("Recognized captcha text:", captcha_text)
        
        # Send the recognized text to the captcha service (hypothetical)
        captcha_service_url = "https://example.com/captcha_verification"
        data = {"captcha_text": captcha_text}
        # Example: response = requests.post(captcha_service_url, data=data)
        print("Captcha verification successful!")
    else:
        print("Failed to recognize captcha text.")

# Example usage:
mp3_file_path = "C:/Users/eddyg/Desktop/Fb/audio.mp3"  # Path to the MP3 recaptcha audio file
solve_recaptcha(mp3_file_path)
