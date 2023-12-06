import tkinter as tk

from controller import AppController


class RecorderApp:
    """
    A class representing the GUI interface for the recorder application.

    This class manages the graphical user interface for recording audio,
    toggling between start and stop recording states, and processing the audio through the controller.

    Attributes:
        root (tk.Tk): The root window for the tkinter application.
        controller (AppController): An instance of AppController to manage recording and processing logic.
        is_recording (bool): A flag to indicate whether recording is currently happening.
        toggle_button (tk.Button): A button in the GUI to start/stop recording.
    """

    def __init__(self, root):
        """
        Initializes the RecorderApp with a tkinter root window and sets up the GUI elements.

        Args:
            root (tk.Tk): The root window for the tkinter application.
        """
        self.root = root
        self.controller = AppController()
        self.is_recording = False
        self.toggle_button = tk.Button(root, text="Start Recording", command=self.toggle_recording)
        self.toggle_button.pack()

    def toggle_recording(self):
        """
        Toggles the recording state between starting and stopping.

        Changes the button text based on the recording state and calls the appropriate
        methods in the controller to start or stop and process the recording.
        """
        if not self.is_recording:
            self.controller.start_recording()
            self.toggle_button.config(text="Stop Recording")
        else:
            self.controller.stop_and_process_recording()
            self.toggle_button.config(text="Start Recording")
        self.is_recording = not self.is_recording


def main():
    """
    Main function to initialize and run the tkinter application.
    """
    root = tk.Tk()
    app = RecorderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
