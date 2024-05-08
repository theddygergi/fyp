# MP3 to WAV Converter for Google Captcha

This script converts MP3 audio files to WAV format, specifically designed for solving audio-based Google Captcha challenges.

## Prerequisites

- Python 3.x installed on your system
- `soundfile` library installed (can be installed via `pip install soundfile`)

## Installation

1. Install the required Python package using pip:

```bash
pip install soundfile
```

## Usage

1. Import the `convert_mp3_to_wav` function from the script.
2. Provide the path to the input MP3 file and the desired path to save the output WAV file.
3. Call the `convert_mp3_to_wav` function with the MP3 file path and WAV file path as arguments.
4. The function returns the converted audio data and the sample rate.

Example:

```python
import soundfile as sf

def convert_mp3_to_wav(mp3_file, wav_file):
    # Read the MP3 file and write it as WAV
    data, sample_rate = sf.read(mp3_file)
    sf.write(wav_file, data, sample_rate)
    
    return data, sample_rate  # Return the converted audio data and the sample rate

# Example usage:
mp3_file = "audio.mp3"  # Path to the MP3 file
wav_file = "output.wav"  # Path to save the WAV file
converted_data, sample_rate = convert_mp3_to_wav(mp3_file, wav_file)

# Now you can use converted_data and sample_rate as needed
```

## Important Note

Make sure to replace `"audio.mp3"` with the path to your input MP3 file and `"output.wav"` with the desired path to save the output WAV file.

``` 