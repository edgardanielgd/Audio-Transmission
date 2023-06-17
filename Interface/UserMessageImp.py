from UserMessage import Ui_Form
from PySide6.QtWidgets import QFrame

class UserMessage(QFrame, Ui_Form):
    def __init__(self, username, child, parent=None):
        QFrame.__init__(self, parent)
        self.setupUi(self)
        self.lblUsername.setText(username)
        self.lytMessage.addWidget(child)