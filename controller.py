import audiorecorder
import chatgpt
import stt
import tts

# Define the path where the audio recording will be saved
RECORDING_PATH = "voice_recordings/output.wav"


class AppController:
    """
    Controller class for managing the application's core functionalities including
    audio recording, speech-to-text processing, chat response generation, and text-to-speech synthesis.
    """

    def __init__(self):
        """
        Initializes the AppController with an AudioRecorder instance.
        """
        self.recorder = audiorecorder.AudioRecorder()

    def start_recording(self):
        """
        Starts the audio recording process using the AudioRecorder instance.
        """
        self.recorder.start_recording()

    def stop_and_process_recording(self):
        """
        Stops the audio recording, saves the recorded file, and initiates the processing of the recording.

        This involves transcribing the audio, getting a response from a chatbot, and synthesizing speech.
        """
        self.recorder.stop_recording()
        self.recorder.save(RECORDING_PATH)
        self.process_recording()

    @staticmethod
    def process_recording():
        """
        Processes the saved recording by transcribing it, obtaining a chatbot response,
        and generating audio from the chatbot's text response.

        The steps are:
        1. Transcribe the audio file to text.
        2. Send the transcribed text to the chatbot for a response.
        3. Use text-to-speech to synthesize the chatbot's response into audio.
        """
        # Transcribe the audio file to text
        transcription = stt.transcribe_from_file(RECORDING_PATH)

        # Get a response from the chatbot based on the transcription
        chatgpt_response = chatgpt.continue_chat(transcription)

        # Synthesize the chatbot's response into audio
        tts.generate_and_play_audio(chatgpt_response)
