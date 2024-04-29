from pydub import AudioSegment
import os

# Function to convert MP3 to WAV
def convert_mp3_to_wav(mp3_file, wav_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)
    
    # Export the audio to WAV format
    audio.export(wav_file, format="wav")

# Example usage
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
    mp3_file = os.path.join(script_dir, "1.mp3")  # Path to the MP3 file in the same directory
    wav_file = os.path.join(script_dir, "1.wav")  # Path to the WAV file (output)

    convert_mp3_to_wav(mp3_file, wav_file)
    print("Conversion completed.")
