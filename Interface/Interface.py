from UserDialogImp import UserDialog
from MainChatImp import MainChat
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QMessageBox
import sys

initial_users = [ "Edgar", "Jhonatan" ]
users = []

# Construct a QApplication
app = QApplication([])
# Create a window and show it

OnAddChatter = lambda a : users.append( a )
    
# Create a main chat window
mainChat = MainChat( OnAddChatter )

# Create a user interface for each user
for user in initial_users:
    dialog = UserDialog( mainChat, user )
    users.append( dialog )
    dialog.show()

mainChat.show()

# Run the event loop
sys.exit(app.exec())