from UserMessage import Ui_Form
from PySide6.QtWidgets import QFrame
from PySide6 import QtWidgets as QWidgets

class UserMessage(QFrame, Ui_Form):
    def __init__(self, username, child, parent=None, is_image = False):
        QFrame.__init__(self, parent)
        self.setupUi(self)
        self.lblUsername.setText(username)
        
        self.childLayout = QWidgets.QVBoxLayout()
        self.childLayout.setContentsMargins( 0,0,0,0 )
        self.childFrame.setLayout( self.childLayout )

        if is_image:
            self.childLayout.setFixedSize( 200, 200 )

        self.childLayout.addWidget( child )