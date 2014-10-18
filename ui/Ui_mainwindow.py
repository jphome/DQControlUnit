# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Oct 18 11:28:57 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(997, 697)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo/media/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 951, 621))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.subControlButton_1 = QtGui.QPushButton(self.tab_1)
        self.subControlButton_1.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.subControlButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subControlButton_1.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/switch/media/auto_.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/switch/media/manul_.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.subControlButton_1.setIcon(icon1)
        self.subControlButton_1.setIconSize(QtCore.QSize(48, 32))
        self.subControlButton_1.setCheckable(True)
        self.subControlButton_1.setObjectName(_fromUtf8("subControlButton_1"))
        self.tempInfo = QtGui.QLCDNumber(self.tab_1)
        self.tempInfo.setEnabled(True)
        self.tempInfo.setGeometry(QtCore.QRect(150, 290, 64, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.tempInfo.setFont(font)
        self.tempInfo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tempInfo.setMouseTracking(False)
        self.tempInfo.setAcceptDrops(False)
        self.tempInfo.setAutoFillBackground(False)
        self.tempInfo.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.tempInfo.setFrameShape(QtGui.QFrame.Box)
        self.tempInfo.setFrameShadow(QtGui.QFrame.Plain)
        self.tempInfo.setSmallDecimalPoint(True)
        self.tempInfo.setNumDigits(5)
        self.tempInfo.setDigitCount(5)
        self.tempInfo.setMode(QtGui.QLCDNumber.Dec)
        self.tempInfo.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.tempInfo.setProperty("value", 5.1)
        self.tempInfo.setObjectName(_fromUtf8("tempInfo"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.subControlButton_2 = QtGui.QPushButton(self.tab_2)
        self.subControlButton_2.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.subControlButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subControlButton_2.setText(_fromUtf8(""))
        self.subControlButton_2.setIcon(icon1)
        self.subControlButton_2.setIconSize(QtCore.QSize(48, 32))
        self.subControlButton_2.setCheckable(True)
        self.subControlButton_2.setObjectName(_fromUtf8("subControlButton_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.subControlButton_3 = QtGui.QPushButton(self.tab_3)
        self.subControlButton_3.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.subControlButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subControlButton_3.setText(_fromUtf8(""))
        self.subControlButton_3.setIcon(icon1)
        self.subControlButton_3.setIconSize(QtCore.QSize(48, 32))
        self.subControlButton_3.setCheckable(True)
        self.subControlButton_3.setObjectName(_fromUtf8("subControlButton_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gControlButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.gControlButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gControlButton.setText(_fromUtf8(""))
        self.gControlButton.setIcon(icon1)
        self.gControlButton.setIconSize(QtCore.QSize(48, 32))
        self.gControlButton.setCheckable(True)
        self.gControlButton.setObjectName(_fromUtf8("gControlButton"))
        self.gridLayout.addWidget(self.gControlButton, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.gControlButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.subControlButton_3.setDisabled)
        QtCore.QObject.connect(self.gControlButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.subControlButton_1.setDisabled)
        QtCore.QObject.connect(self.gControlButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.subControlButton_2.setDisabled)
        QtCore.QObject.connect(self.gControlButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.subControlButton_1.setChecked)
        QtCore.QObject.connect(self.gControlButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.subControlButton_2.setChecked)
        QtCore.QObject.connect(self.gControlButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.subControlButton_3.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "主控界面", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "金银花提取", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "连翘提取", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "页3", None))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

