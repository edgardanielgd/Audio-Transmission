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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(281, 62)
        Form.setStyleSheet(u"background-color: black;\n"
"border-radius: 10px;")
        self.lblUsername = QLabel(Form)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setGeometry(QRect(10, 20, 51, 16))
        self.lblUsername.setStyleSheet(u"color: white;\n"
"border-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.lblUsername.setAlignment(Qt.AlignCenter)
        self.frmData = QFrame(Form)
        self.frmData.setObjectName(u"frmData")
        self.frmData.setGeometry(QRect(70, 10, 201, 51))
        self.frmData.setStyleSheet(u"color: white;\n"
"background: none;\n"
"background:transparent;")
        self.frmData.setFrameShape(QFrame.StyledPanel)
        self.frmData.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frmData)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lytMessage = QVBoxLayout()
        self.lytMessage.setObjectName(u"lytMessage")

        self.verticalLayout.addLayout(self.lytMessage)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblUsername.setText(QCoreApplication.translate("Form", u"Username", None))
    # retranslateUi

