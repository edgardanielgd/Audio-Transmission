# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainChat.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLayout,
    QPushButton, QScrollArea, QSizePolicy, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)
import ChatterBackground_rc

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(515, 424)
        Frame.setStyleSheet(u"background-image: url(:/Background/chatbackground.jpg)")
        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 141, 31))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush2 = QBrush(QColor(255, 255, 220, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        self.label.setPalette(palette)
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
        self.tabWidget = QTabWidget(Frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 30, 471, 341))
        self.tabWidget.setStyleSheet(u"background: none;\n"
"background-color: black;")
        self.tabChat = QWidget()
        self.tabChat.setObjectName(u"tabChat")
        self.ChatBody = QScrollArea(self.tabChat)
        self.ChatBody.setObjectName(u"ChatBody")
        self.ChatBody.setGeometry(QRect(10, 10, 441, 291))
        self.ChatBody.setStyleSheet(u"")
        self.ChatBody.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 439, 289))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainLayout = QVBoxLayout()
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setSizeConstraint(QLayout.SetFixedSize)

        self.verticalLayout.addLayout(self.MainLayout)

        self.ChatBody.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tabChat, "")
        self.tabLogs = QWidget()
        self.tabLogs.setObjectName(u"tabLogs")
        self.scrollArea = QScrollArea(self.tabLogs)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 441, 151))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 439, 149))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 421, 131))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.drwGeneralChatsLog = QLabel(self.verticalLayoutWidget)
        self.drwGeneralChatsLog.setObjectName(u"drwGeneralChatsLog")
        self.drwGeneralChatsLog.setStyleSheet(u"background: none;\n"
"background-color: white;")

        self.verticalLayout_2.addWidget(self.drwGeneralChatsLog)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.txtGeneralChatLogs = QTextEdit(self.tabLogs)
        self.txtGeneralChatLogs.setObjectName(u"txtGeneralChatLogs")
        self.txtGeneralChatLogs.setGeometry(QRect(10, 170, 441, 121))
        self.txtGeneralChatLogs.setStyleSheet(u"color: white;")
        self.txtGeneralChatLogs.setReadOnly(True)
        self.tabWidget.addTab(self.tabLogs, "")
        self.btnAddChatter = QPushButton(Frame)
        self.btnAddChatter.setObjectName(u"btnAddChatter")
        self.btnAddChatter.setGeometry(QRect(350, 380, 111, 30))
        self.btnAddChatter.setStyleSheet(u"QPushButton {\n"
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
        self.txtNewUserName = QTextEdit(Frame)
        self.txtNewUserName.setObjectName(u"txtNewUserName")
        self.txtNewUserName.setGeometry(QRect(193, 380, 151, 31))
        self.txtNewUserName.setStyleSheet(u"background: none;\n"
"background-color: black;\n"
"color: white;")

        self.retranslateUi(Frame)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Main Chat", None))
        self.label.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Chat Principal</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabChat), QCoreApplication.translate("Frame", u"Chat", None))
        self.drwGeneralChatsLog.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLogs), QCoreApplication.translate("Frame", u"Logs", None))
        self.btnAddChatter.setText(QCoreApplication.translate("Frame", u"A\u00f1adir Miembro", None))
    # retranslateUi

