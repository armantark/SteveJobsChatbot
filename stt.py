import os

from deepgram import Deepgram
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the Deepgram API key from the environment variables
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

# Initialize the Deepgram client with the API key
deepgram = Deepgram(DEEPGRAM_API_KEY)


def transcribe_from_file(path):
    """
    Transcribes audio from a file using the Deepgram API.

    This function opens an audio file, sends it to Deepgram for transcription, and retrieves the text transcription.

    Args:
        path (str): The file path to the audio file to be transcribed.

    Returns:
        str: The transcribed text of the audio file.
    """
    # Open the audio file in binary read mode
    with open(path, 'rb') as audio:
        # Define the source with the audio file and its MIME type
        source = {'buffer': audio, 'mimetype': 'audio/wav'}

        # Send the audio for transcription and receive the response
        response = deepgram.transcription.sync_prerecorded(source, {'smart_format': True, 'punctuate': True})

        # Extract and return the transcribed text from the response
        return response["results"]["channels"][0]["alternatives"][0]["transcript"]
