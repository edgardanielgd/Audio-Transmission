# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserMessage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(398, 106)
        Form.setMinimumSize(QSize(398, 106))
        Form.setStyleSheet(u"background-color: black;\n"
"border-radius: 10px;")
        self.lblUsername = QLabel(Form)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setGeometry(QRect(10, 30, 91, 30))
        self.lblUsername.setStyleSheet(u"color: white;\n"
"border-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.lblUsername.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(120, 10, 251, 81))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 251, 81))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.childFrame = QFrame(self.scrollAreaWidgetContents)
        self.childFrame.setObjectName(u"childFrame")
        self.childFrame.setFrameShape(QFrame.StyledPanel)
        self.childFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.childFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblUsername.setText(QCoreApplication.translate("Form", u"Username", None))
    # retranslateUi

