import soundfile as sf

def convert_mp3_to_wav(mp3_file, wav_file):
    # Read the MP3 file and write it as WAV
    data, sample_rate = sf.read(mp3_file)
    sf.write(wav_file, data, sample_rate)
    
    return data, sample_rate  # Return the converted audio data and the sample rate
    
# Example usage:
#mp3_file = "audio.mp3"  # Path to the MP3 file
#wav_file = "output.wav"  # Path to save the WAV file
#converted_data, sample_rate = convert_mp3_to_wav(mp3_file, wav_file)

# Now you can use converted_data and sample_rate as needed
