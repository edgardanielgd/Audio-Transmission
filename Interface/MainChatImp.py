from MainChat import Ui_Frame
from PySide6.QtWidgets import QDialog
import PySide6.QtWidgets as QtWidgets

class MainChat(QDialog, Ui_Frame):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
    
    def receiveText(self, username, text ):
        # Create a new component for the text
        lbl = QtWidgets.QLabel(  )
        lbl.setText( "<b>" + username + "</br> : " + text )
        lbl.setWordWrap(True)
        lbl.setFixedWidth( self.ChatBody.width() - 20 )
        lbl.setFixedHeight( lbl.sizeHint().height() )   
        lbl.setStyleSheet(
            """
                background-color: rgb(255, 255, 255) !important; 
                color: rgb(255, 255, 255) !important; 
                border-radius: 10px;
            """
        )
        
        # Add the component to ChatBody (Which is a scroll area)
        self.MainLayout.addWidget( lbl )
        

