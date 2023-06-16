from UserDialog import Ui_Frame
from PySide6.QtWidgets import QDialog, QFileDialog
from Utils import configStyleSheet
import pyaudio
import wave
import numpy as np

class UserDialog(QDialog, Ui_Frame):
    def __init__(self, parentChat, username ):
        QDialog.__init__(self)
        self.parentChat = parentChat
        self.setupUi(self)
        self.username = username

        self.lblUsername.setText(self.username)

        self.btnSend.clicked.connect(self.send)
        self.btnSendImage.clicked.connect(self.sendImage)
        self.btnAudioRecord.clicked.connect(self.audioRecord)

        self.setWindowTitle("ChatBox of " + self.username)

        # Audio Recording settings
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.p = None
        self.stream = None
        self.frames = []

        self.recording = False

    def send(self):
        print("Enviando pa " , self.username )
        self.parentChat.receiveText( self.username, self.txtMessageText.toPlainText() )
    
    def sendImage(self):
        # Ask user for the path of target image
        dialog = QFileDialog()
        dialog.setStyleSheet(
            """
                background: none;
                background-color: black;
                color:white;
            """
        )
        dialog.setWindowTitle('Choose the image you want to send')
        dialog.setFileMode(QFileDialog.ExistingFile)
        
        if dialog.exec() == QFileDialog.Accepted:
            path = dialog.selectedFiles()[0]
            print( path )

        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # fileName, _ = QFileDialog.getOpenFileName(
        #     self, "Choose an image to upload!", 
        #     "", "All Files (*);;Python Files (*.py)", options=options)
        # if fileName:
        #     print(fileName)
    
    def audioRecord(self):
        if self.recording :
            # Stop recording audio
            output_file = "recorded.wav"
            # wf = wave.open(output_file, "wb")
            # wf.setnchannels(self.CHANNELS)
            # wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            # wf.setframerate(self.RATE)
            # wf.writeframes(b''.join(self.frames))
            # wf.close()

            p = pyaudio.PyAudio()
            stream = self.p.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                output=True
            )
            
            for frame in self.frames:
                stream.write( frame )

            stream.close()
            p.terminate()

            self.stream.close()
            self.p.terminate()
            self.stream = None
            self.p = None

            self.btnAudioRecord.setText("Grabar Audio")
        else:
            # Start recording audio
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                stream_callback=self.audioRecordcallback,
                frames_per_buffer=self.CHUNK
            )
            self.btnAudioRecord.setText("Detener Grabación")
            
        self.recording = not self.recording
        self.btnAudioRecord.setStyleSheet(configStyleSheet( self.recording ))

    def audioRecordcallback(self, data, frame_count, time_info, status):
        data = np.fromstring(data, 'int32')
        self.frames.append(data)
        return None, pyaudio.paContinue

        