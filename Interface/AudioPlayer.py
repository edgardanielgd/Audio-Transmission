from PySide6.QtCore import QThread
import wave
import pyaudio

class AudioPlayer(QThread):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def run(self):
        p = pyaudio.PyAudio()

        chunk = 1024

        wf = wave.open(self.path, 'rb')
        stream = p.open(
                format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True
            )
        # Read data in chunks
        data = wf.readframes(chunk)

        # Play the sound by writing the audio data to the stream
        while data != '':
            stream.write(data)
            data = wf.readframes(chunk)

        # Close and terminate the stream
        stream.close()
        p.terminate()