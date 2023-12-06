import wave

import numpy as np
import sounddevice as sd


class AudioRecorder:
    """
    A class to handle audio recording using the sounddevice library.

    Attributes:
        channels (int): The number of channels in the audio recording (e.g., 1 for mono, 2 for stereo).
        rate (int): The sample rate of the audio recording in Hz.
        record_seconds (int): The duration of the audio recording in seconds.
        frames (list): A list to store audio frames captured during recording.
        recording (bool): A flag to indicate whether recording is currently happening.
        stream (sounddevice.InputStream): The input stream for audio recording.
    """

    def __init__(self, channels=1, rate=44100, record_seconds=5):
        """
        Initializes the AudioRecorder with specified audio settings.

        Args:
            channels (int): Number of audio channels. Default is 1 (mono).
            rate (int): Sampling rate in Hz. Default is 44100 Hz.
            record_seconds (int): Duration of recording in seconds. Default is 5 seconds.
        """
        self.stream = None
        self.channels = channels
        self.rate = rate
        self.record_seconds = record_seconds
        self.frames = []
        self.recording = False

    def callback(self, indata, frames, time, status):
        """
        Callback function for the sounddevice input stream.

        This function is called for each block of audio data, appending it to the frames list if recording is active.

        Args:
            indata (numpy.ndarray): The buffer containing the incoming audio frame.
            frames (int): Number of frames in the current audio block.
            time (CData): Current stream time.
            status (CallbackFlags): Indicates any errors or events.
        """
        if self.recording:
            self.frames.append(indata.copy())

    def start_recording(self):
        """
        Starts the audio recording process.

        Initializes and starts the input stream, and sets the recording flag to True.
        """
        self.frames = []
        self.recording = True
        self.stream = sd.InputStream(callback=self.callback, channels=self.channels, samplerate=self.rate)
        self.stream.start()

    def stop_recording(self):
        """
        Stops the audio recording process.

        Sets the recording flag to False and stops the input stream.
        """
        self.recording = False
        self.stream.stop()

    def save(self, filename):
        """
        Saves the recorded audio to a file.

        Args:
            filename (str): The path and filename where the audio will be saved.
        """
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setframerate(self.rate)
        wf.setsampwidth(2)  # 16-bit PCM format
        pcm_data = np.concatenate(self.frames) * 32767  # Convert to 16-bit PCM
        pcm_data = pcm_data.astype(np.int16)  # Ensure the data is in int16 format
        wf.writeframes(pcm_data.tobytes())
        wf.close()
