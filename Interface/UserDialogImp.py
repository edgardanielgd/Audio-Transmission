from UserDialog import Ui_Frame
from PySide6.QtWidgets import QDialog

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

    def send(self):
        print("Enviando pa " , self.username )
        self.parentChat.receiveText( self.username, self.txtMessageText.toPlainText() )
    
    def sendImage(self):
        print("Enviando imagen pa ", self.username )
    
    def audioRecord(self):
        print("Grabando audio pa ", self.username )


        