import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks

def mp3_to_text(mp3_file_path):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file_path)

    # Convert stereo to mono
    audio = audio.set_channels(1)

    # Split audio into chunks for better recognition
    chunk_length_ms = 10000  # split into 10-second chunks
    chunks = make_chunks(audio, chunk_length_ms)

    recognizer = sr.Recognizer()

    # Initialize empty text
    text = ""

    # Process each chunk
    for i, chunk in enumerate(chunks):
        chunk_name = f"chunk{i}.wav"
        chunk.export(chunk_name, format="wav")

        with sr.AudioFile(chunk_name) as source:
            audio_data = recognizer.record(source)

        # Recognize the chunk
        try:
            chunk_text = recognizer.recognize_google(audio_data)
            text += chunk_text + " "
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    return text.strip()

# Example usage:
mp3_file_path = "C:/Users/eddyg/Desktop/Fb/audio.mp3"  # Replace with your MP3 file path
transcription = mp3_to_text(mp3_file_path)
print("Transcription:")
print(transcription)
