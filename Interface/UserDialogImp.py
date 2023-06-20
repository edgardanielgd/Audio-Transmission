from UserDialog import Ui_Frame
from PySide6.QtWidgets import QDialog, QFileDialog
from Utils import Audio, Images, Text, Huffman
from Utils.Misc import *
from PIL import Image
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

        # Fill up combobox with possible options
        self.cmbEncoders.addItems( [
            "Huffman"
        ] )

        # If main chat window is closed, close this window too
        self.parentChat.destroyed.connect( self.close )

        self.setWindowTitle("ChatBox of " + self.username)

        # Audio Recording settings
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.p = None
        self.stream = None
        self.frames = []

        self.recording = False

    def send(self):

        # Parse text to numbers
        vector = Text.convertTextToVector( self.txtMessageText.toPlainText() )

        # Get encoded data
        data = self.encodeData( vector )

        data["type"] = "text"

        self.parentChat.receiveData( data )

        # self.parentChat.addText( self.username, self.txtMessageText.toPlainText() )
    
    def sendImage(self):

        registerLog( "Enviando imagen", self.txtLog)

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
        
        if dialog.exec() != QFileDialog.Accepted:
            return
        
        path = dialog.selectedFiles()[0]

        # Read the image
        
        image = Image.open( path )

        # Parse text to numbers
        vector = Images.convertImageToVector( image )
        
        # Send the image
        self.parentChat.addImage( self.username, image )

    def audioRecord(self):
        if self.recording :
            # Call parent receiver for this info
            self.parentChat.receiveAudio( 
                self.username, self.frames, 
                self.FORMAT, self.CHANNELS, self.RATE 
            )

            # Parse audio to levels
            levels, quantification_dict = Audio.convertAudioToVector( self.frames )

            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()

            self.stream = None
            self.p = None
            self.frames = []

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
        data = np.fromstring(data, 'int16')
        self.frames.extend(data)
        return None, pyaudio.paContinue

    def encodeData(self, data, **kwargs):
        # Data should come as a numpy array of discrete values
        # We will take care of each method and use different encoding schemes

        method = self.cmbEncoders.currentText()
        data_return = {
            "method" : method,
            "username" : self.username,
        }

        if method == "Huffman":
            # Huffman encoding

            # Encode data with huffman
            encoding_tree, bits_encoded = Huffman.encode_huffman( data )

            # We have all needed info to decode this data on
            # Main Chat wiew
            data_return.update( {
                "data" : bits_encoded,
                "encoding_tree" : encoding_tree
            })
        
        return data_return

