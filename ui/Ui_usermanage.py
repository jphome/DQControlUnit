# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usermanage.ui'
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

class Ui_UserManageDialog(object):
    def setupUi(self, UserManageDialog):
        UserManageDialog.setObjectName(_fromUtf8("UserManageDialog"))
        UserManageDialog.resize(290, 210)
        self.buttonBox = QtGui.QDialogButtonBox(UserManageDialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 150, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(UserManageDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(UserManageDialog)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(UserManageDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), UserManageDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), UserManageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UserManageDialog)

    def retranslateUi(self, UserManageDialog):
        UserManageDialog.setWindowTitle(_translate("UserManageDialog", "用户管理", None))
        self.label.setText(_translate("UserManageDialog", "管理员", None))
        self.label_2.setText(_translate("UserManageDialog", "admin", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UserManageDialog = QtGui.QDialog()
    ui = Ui_UserManageDialog()
    ui.setupUi(UserManageDialog)
    UserManageDialog.show()
    sys.exit(app.exec_())

