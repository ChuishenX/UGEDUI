# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(678, 360)
        icon = QIcon()
        icon.addFile(u"../A.icns", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.preload = QLabel(self.centralwidget)
        self.preload.setObjectName(u"preload")
        self.preload.setGeometry(QRect(20, 20, 221, 121))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.preload.setFont(font)
        self.preload.setAlignment(Qt.AlignCenter)
        self.theInput = QPlainTextEdit(self.centralwidget)
        self.theInput.setObjectName(u"theInput")
        self.theInput.setGeometry(QRect(10, 160, 651, 181))
        self.converter = QPushButton(self.centralwidget)
        self.converter.setObjectName(u"converter")
        self.converter.setGeometry(QRect(260, 80, 401, 51))
        self.downloader = QPushButton(self.centralwidget)
        self.downloader.setObjectName(u"downloader")
        self.downloader.setGeometry(QRect(260, 20, 401, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UGEDUI(\u6709\u4e2a\u5806)", None))
        self.preload.setText(QCoreApplication.translate("MainWindow", u"UGEDUI", None))
        self.theInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740(\u5206\u884c)", None))
        self.converter.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u4e3aMP3", None))
        self.downloader.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6587\u4ef6", None))
    # retranslateUi

