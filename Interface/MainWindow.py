import tkinter as tk
from tkinter import ttk
import soundfile as sf
import pyaudio
import librosa
import wave
import numpy as np

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Transmisión de audio")
        self.geometry("800x600")
        self.resizable(False, False)

        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 2
        self.p = None
        self.stream = None
        self.recording = False
        self.data = []

        # Create a frame for the buttons
        self.button = tk.Button(self, text="Grabar", command=self.record)
        self.button.pack()

        # Create a label for letting user know about the current state
        self.label = tk.Label(self, text="Estado: No grabando")
        self.label.pack()

    def record(self):
        if not self.recording:
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                output=False,
                stream_callback=self.callback,
                frames_per_buffer=self.CHUNK
            )
            self.label["text"] = "Estado: Grabando"
        else:

            # Save recorded data to a file
            # sf.write(
            #     "Outputs/test.wav", 
            #     np.array(self.data), 
            #     samplerate = 44100,
            #     format="WAV"
            # )
            output_file = "recorded.wav"
            wf = wave.open(output_file, "wb")
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.data))
            wf.close()

            self.stream.close()
            self.p.terminate()
            self.stream = None
            self.p = None
            self.label["text"] = "Estado: No grabando"
            
            self.data = []

        self.recording = not self.recording
    
    def callback(self, in_data, frame_count, time_info, status):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        self.data.append(numpy_array)
        return None, pyaudio.paContinue

window = MainWindow()
window.mainloop()