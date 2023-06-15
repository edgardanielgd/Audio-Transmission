from UserDialogImp import UserDialog
from MainChatImp import MainChat
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QMessageBox
import sys

users = [ "Jhonatan", "Edgar", "Miguel" ]
chatters = []

# Construct a QApplication
app = QApplication([])
# Create a window and show it

# Create a main chat window
mainChat = MainChat( )

# Create a user interface for each user
for user in users:
    dialog = UserDialog( mainChat, user )
    chatters.append( dialog )
    dialog.show()

mainChat.show()

# Run the event loop
sys.exit(app.exec())

