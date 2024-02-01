# text_to_speech.py

from gtts import gTTS
import os


def text_to_speech(text, language='en', output_file='output.mp3'):
    """
    Converts text to speech and saves it as an audio file.

    Parameters:
    - text (str): The text to be converted to speech.
    - language (str): The language of the text. Default is English ('en').
    - output_file (str): The name of the output audio file. Default is 'output.mp3'.
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)

    # Play the generated audio file (optional)
    os.system(f"open {output_file}")


# Example usage:
if __name__ == "__main__":
    text_to_speech("Hello, this is a test.")
