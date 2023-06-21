# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import ChatterBackground_rc

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(510, 422)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(104, 240, 66, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(193, 255, 175, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(148, 247, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(52, 120, 33, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(69, 160, 44, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(255, 170, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        brush8 = QBrush(QColor(35, 255, 32, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(179, 247, 160, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        brush10 = QBrush(QColor(255, 255, 220, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush11 = QBrush(QColor(0, 120, 215, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        Frame.setPalette(palette)
        Frame.setAutoFillBackground(False)
        Frame.setStyleSheet(u"background-image: url(:/Background/chatbackground.jpg)")
        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 171, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.label.setPalette(palette1)
        font = QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background: none;\n"
"background-color: black;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 1px;\n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.btnAudioRecord = QPushButton(Frame)
        self.btnAudioRecord.setObjectName(u"btnAudioRecord")
        self.btnAudioRecord.setGeometry(QRect(60, 140, 101, 21))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btnAudioRecord.setPalette(palette2)
        font1 = QFont()
        font1.setPointSize(6)
        self.btnAudioRecord.setFont(font1)
        self.btnAudioRecord.setStyleSheet(u"QPushButton {\n"
"	background: none;\n"
"	background-color: black;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: white;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: white;\n"
"	border-color: black;\n"
"	color: black;\n"
"}")
        self.txtMessageText = QPlainTextEdit(Frame)
        self.txtMessageText.setObjectName(u"txtMessageText")
        self.txtMessageText.setGeometry(QRect(300, 70, 191, 40))
        self.txtMessageText.setFont(font1)
        self.txtMessageText.setStyleSheet(u"background: none;\n"
"background-color: black;\n"
"color: white;")
        self.label_3 = QLabel(Frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 120, 191, 20))
        self.label_3.setStyleSheet(u"background: none;\n"
"background-color: black;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 1px;\n"
"color: white;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.btnSend = QPushButton(Frame)
        self.btnSend.setObjectName(u"btnSend")
        self.btnSend.setGeometry(QRect(380, 150, 71, 17))
        self.btnSend.setFont(font1)
        self.btnSend.setStyleSheet(u"QPushButton {\n"
"	background: none;\n"
"	background-color: black;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: white;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: white;\n"
"	border-color: black;\n"
"	color: black;\n"
"}")
        self.btnSendImage = QPushButton(Frame)
        self.btnSendImage.setObjectName(u"btnSendImage")
        self.btnSendImage.setGeometry(QRect(170, 140, 91, 21))
        self.btnSendImage.setFont(font1)
        self.btnSendImage.setStyleSheet(u"QPushButton {\n"
"	background: none;\n"
"	background-color: black;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: white;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: white;\n"
"	border-color: black;\n"
"	color: black;\n"
"}")
        self.lblUsername = QLabel(Frame)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setGeometry(QRect(210, 0, 231, 71))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush12 = QBrush(QColor(0, 0, 0, 0))
        brush12.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        self.lblUsername.setPalette(palette3)
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(25)
        self.lblUsername.setFont(font2)
        self.lblUsername.setStyleSheet(u"background: none;\n"
"background: transparent;")
        self.lblUsername.setTextFormat(Qt.PlainText)
        self.lblUsername.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(30, 200, 441, 131))
        self.scrollArea.setStyleSheet(u"background: none;\n"
"background-color: black;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 439, 129))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logContainer = QFrame(self.scrollAreaWidgetContents)
        self.logContainer.setObjectName(u"logContainer")
        self.logContainer.setFrameShape(QFrame.StyledPanel)
        self.logContainer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.logContainer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.txtLog = QTextEdit(Frame)
        self.txtLog.setObjectName(u"txtLog")
        self.txtLog.setGeometry(QRect(30, 340, 441, 71))
        self.txtLog.setStyleSheet(u"background: none;\n"
"background-color: black;\n"
"color: white;")
        self.txtLog.setReadOnly(True)
        self.label_4 = QLabel(Frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 170, 191, 20))
        self.label_4.setStyleSheet(u"background: none;\n"
"background-color: black;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 1px;\n"
"color: white;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.cmbEncoders = QComboBox(Frame)
        self.cmbEncoders.setObjectName(u"cmbEncoders")
        self.cmbEncoders.setGeometry(QRect(100, 100, 111, 22))
        self.cmbEncoders.setStyleSheet(u"background: none;\n"
"background-color: gray;\n"
"color: black;")
        self.label_5 = QLabel(Frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 70, 231, 20))
        self.label_5.setStyleSheet(u"background: none;\n"
"background-color: black;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 1px;\n"
"color: white;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 180, 161, 16))
        self.label_2.setStyleSheet(u"background: none;\n"
"background: transparent;")

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"ChatBox of Username", None))
        self.label.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Panel de usuario:</span></p></body></html>", None))
        self.btnAudioRecord.setText(QCoreApplication.translate("Frame", u"Grabar Audio", None))
        self.label_3.setText(QCoreApplication.translate("Frame", u"Escribe un mensaje y env\u00edalo!", None))
        self.btnSend.setText(QCoreApplication.translate("Frame", u"Enviar", None))
        self.btnSendImage.setText(QCoreApplication.translate("Frame", u"Enviar imagen", None))
        self.lblUsername.setText(QCoreApplication.translate("Frame", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Frame", u"Logs", None))
        self.label_5.setText(QCoreApplication.translate("Frame", u"Selecciona el codificador a usar", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p><a href=\"https://elcodigoascii.com.ar/\">Tabla ASCII</a></p></body></html>", None))
    # retranslateUi

