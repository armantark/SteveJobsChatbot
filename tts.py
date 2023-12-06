import os

from dotenv import load_dotenv
from elevenlabs import generate, stream, set_api_key

# Load environment variables from a .env file
load_dotenv()

# Set the ElevenLabs API key from the environment variables
set_api_key(os.getenv("ELEVENLABS_API_KEY"))


def generate_and_play_audio(text):
    """
    Generates audio from text using the ElevenLabs API and streams the audio.

    This function takes a text string, converts it to audio using ElevenLabs's text-to-speech service,
    and then plays the audio.

    Args:
        text (str): The text to be converted into speech.
    """
    # Generate audio from the provided text using ElevenLabs
    audio = generate(
        text=text,
        voice="Arnold",  # The voice model to use. Can be changed as needed.
        # I just picked this one because I don't have access to premium features for his actual voice.
        model="eleven_multilingual_v2",  # The specific TTS model to use.
        stream=True  # Set to stream the audio directly.
    )

    # Stream the generated audio
    stream(audio)
