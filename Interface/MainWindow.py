import tkinter as tk
from tkinter import ttk
import soundfile as sf
import pyaudio
import librosa
import wave
import numpy as np

class UserPanel(tk.Frame):
    def __init__(self, parent, username, shared_chat):
        super().__init__( parent )
        self.shared_chat = shared_chat
        self.username = username

        self.FORMAT = pyaudio.paFloat16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.p = None
        self.stream = None
        self.recording = False
        self.data = []

        # Create a label for the username
        self.label = tk.Label(self, text=username)
        self.label.pack()

        # Create a frame for the buttons
        self.button = tk.Button(self, text="Grabar", command=self.record)
        self.button.pack()

        # Create a label for letting user know about the current state
        self.label = tk.Label(self, text="Estado: No grabando")
        self.label.pack()

        # Create a text box for the user to enter the message
        self.textbox = tk.Text(self, height=10, width=50)
        self.textbox.pack()

        # Create a button to send the message
        self.button = tk.Button(self, text="Enviar", command=self.send)
        self.button.pack()

    def send(self):
        # Get the message from the textbox
        message = self.textbox.get("1.0", tk.END)

        # Send the message to the server
        # ...
        self.shared_chat.receiveMessage(message, self.username)

        # Clear the textbox
        self.textbox.delete("1.0", tk.END)

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

class CommunicationPanel(tk.Frame):
    def __init__(self, parent ):
        super().__init__( parent )

        # Create a label for letting users know this is the shared chat
        self.label = tk.Label(self, text="Chat compartido")
        self.label.pack()

        # Crear un contenedor scrollable para los mensajes
        self.scrollable_frame = tk.Frame(self)
        self.scrollable_frame.pack()

        # Crear un scrollbar para el contenedor
        self.scrollbar = tk.Scrollbar(self.scrollable_frame)
        self.scrollbar.pack(side="right", fill="y")

        # Crear un canvas para el contenedor
        self.canvas = tk.Canvas(self.scrollable_frame, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Configurar el scrollbar para que se mueva con el canvas
        self.scrollbar.config(command=self.canvas.yview)

    def receiveMessage(self, message, username):
        # Obtener el texto del mensaje y el nombre de usuario
        # mostrarlo en el panel de mensajes
        username_label = tk.Label(self.canvas, text=f"{username} : {message}")
        username_label.pack()

        # Actualizar el canvas
        self.canvas.update_idletasks()

        # Mover el scrollbar al final del canvas
        self.canvas.yview_moveto(1)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Transmisión de audio")
        self.geometry("800x600")
        self.resizable(False, False)

        # Crear un frame scrollable general
        self.scrollable_frame = tk.Frame(self)
        self.scrollable_frame.pack()

        # Crear un scrollbar general
        self.scrollbar = tk.Scrollbar(self.scrollable_frame)
        self.scrollbar.pack(side="right", fill="y")

        shared_chat = CommunicationPanel( self.scrollable_frame )
        shared_chat.pack()

        user1 = UserPanel( self.scrollable_frame, "Edgar", shared_chat )
        user1.pack()

        user2 = UserPanel( self.scrollable_frame, "Naty", shared_chat )
        user2.pack()


window = MainWindow()
window.mainloop()