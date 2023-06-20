from MainChat import Ui_Frame
from UserDialogImp import UserDialog
from UserMessageImp import UserMessage
from multiprocessing import Process
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QImage, QPixmap
from PySide6 import QtCore
from PIL.ImageQt import ImageQt
from Utils import Audio, Images, Text, Huffman
from Utils.Misc import *
from AudioPlayer import AudioPlayer
from Utils.ErrorControl import decodificar_palabra

import PySide6.QtWidgets as QtWidgets
import pyaudio
import wave 
import uuid

class MainChat(QDialog, Ui_Frame):
    def __init__(self, OnAddChatter):
        QDialog.__init__(self)        
        self.setupUi(self)
        self.OnAddChatter = OnAddChatter
        self.btnAddChatter.clicked.connect(self.addChatter)

        self.chatBodyContentsLayout = QtWidgets.QVBoxLayout()
        self.chatBodyContentsLayout.setContentsMargins( 0,0,0,0 )
        
        self.ChatBodyContents.setLayout( self.chatBodyContentsLayout )

        # It is necessary to save a reference to the messages
        # in order to prevent garbage collector from deleting them
        self.messages = []
    
    def addChatter(self):
        # Add a new chatter to the conversation, we will just create 
        # a new instance of UserDialog

        # Get username from adjacent textbox
        username = self.txtNewUserName.toPlainText()
        self.txtNewUserName.clear()

        newUser = UserDialog(self, username)

        # We must save a reference to window in order to
        # prevent garbage collector from deleting our stuff!
        self.OnAddChatter( newUser )
        newUser.show()
    
    def receiveAudio(self, username, frames, format, channels, rate ):
        # Create a random ID for this file
        ID = str(uuid.uuid4())
        waveOutputFile = "./Audios/" + ID + ".wav"

        # In this way we can reproduce the audio from a button click
        # by just reading the file

        p = pyaudio.PyAudio()

        wf = wave.open(waveOutputFile, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b"".join(frames))
        wf.close()

        # Now render a button with a button which will help playing audio file
        btn = QtWidgets.QPushButton()
        btn.setText(">>> Reproducir audio")
        btn.setStyleSheet(
            """
                QPushButton {{
                    background: none;
                    background-color: black;
                    color: white;
                    border-radius: 10px;
                    border-color: white;
                    border-width: 1px;
                    border-style: solid;
                }}

                QPushButton:hover {{
                    background-color: white;
                    color: black;
                    border-color: black;
                }}
            """
        )

        btn.clicked.connect(
            lambda : self.playAudio( waveOutputFile )
        )

        message = UserMessage( username, btn, self )
        
        # Add the component to ChatBody (Which is a scroll area)
        self.chatBodyContentsLayout.addWidget( message )

    def addText(self, username, text ):
        # Create a new component for the text
        lbl = QtWidgets.QLabel(  )
        lbl.setText( text )
        lbl.setWordWrap(True)
        lbl.setFixedHeight( lbl.sizeHint().height() )   
        lbl.setStyleSheet(
            """
                background-color: black; 
                color: white;
                border-radius: 10px;
            """
        )

        message = UserMessage( username, lbl, self.tabChat )

        # Add the component to ChatBody (Which is a scroll area)
        self.chatBodyContentsLayout.addWidget( message )
        
    
    def addImage(self, username, imageObj ):
        # Create a new component for the image
        lbl = QtWidgets.QLabel(  )
        pil2Qt = ImageQt( imageObj )
        qPixMap = QPixmap.fromImage( pil2Qt )
        pixmapImage = QPixmap( qPixMap )

        lbl.setPixmap( pixmapImage )
        lbl.setAlignment( QtCore.Qt.AlignCenter )
        lbl.setScaledContents( True )
        lbl.setFixedSize(
            imageObj.width, imageObj.height
        )
        lbl.setSizePolicy( QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored )
        
        message = UserMessage( username, lbl, self )

        # Add the component to ChatBody (Which is a scroll area)
        self.chatBodyContentsLayout.addWidget( message )
    
    def playAudio(self, path):
        
        self.audio_player = AudioPlayer( path )
        self.audio_player.start()

    def receiveData(self, data):
        # First than all, decode data depending on the encoding algorithm
        # used

        method = data["method"]
        username = data["username"]

        if method == "Huffman":
            # Remove error control data
            bits = data["data"]
            bits, logs = decodificar_palabra( bits )

            for log in logs:
                registerLog( log, self.txtGeneralChatLogs)
            
            bits = bits.tolist()

            # Binary list to string
            bits = "".join( [ str(x) for x in bits ] )

            # Get additional data
            encoding_tree = data["encoding_tree"]
            decoded_data = Huffman.decode_huffman_input( encoding_tree, bits )

        
        # Having data decoded, re shape and format to correct media type
        if data["type"] == "text":
            text = Text.buildTextFromVector( decoded_data )

            registerLog( "Recibiendo texto: " + text, self.txtGeneralChatLogs)

            self.addText( username, text )

        elif data["type"] == "image":
            width = data["width"]
            height = data["height"]
            
            image = Images.buildImageFromVector( decoded_data, width, height )

            registerLog( "Recibiendo imagen: ", self.txtGeneralChatLogs)

            self.addImage( username, image )
        elif data["type"] == "audio":
            audio = Audio.buildAudioFromVector( 
                decoded_data, data["quantification_dict"]
            )

            registerLog( "Recibiendo audio", self.txtGeneralChatLogs)
            
            self.receiveAudio( 
                username, audio, data["format"], 
                data["channels"], data["rate"] 
            )
            