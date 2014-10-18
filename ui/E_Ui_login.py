# -*- coding: utf-8 -*-

"""
Module implementing LoginDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore,  QtGui

from Ui_login import Ui_LoginDialog

class LoginDialog(QDialog, Ui_LoginDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None, authpair = {'admin':'12345'}):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.authpair = authpair
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        b_fail = False
        if self.username.text() and self.password.text():
            # if unicode(self.username.text()) == u'admin' and unicode(self.password.text()) == u'12345':
            if self.authpair.has_key(unicode(self.username.text())):
                if self.authpair[unicode(self.username.text())] == unicode(self.password.text()):
                    self.accept()
                else:
                    # print "密码错误"
                    b_fail = True
                    err_msg = u"密码错误"
                    self.password.clear()
            else:
                # print "用户名不存在"
                b_fail = True
                err_msg = u"用户名不存在"
                self.username.clear()
                self.password.clear()
        else:
            # print "验证信息不完整"
            b_fail = True
            err_msg = u"验证信息不完整"

        if b_fail:
            # message = QtGui.QMessageBox(self)
            # message.setText(err_msg)
            # message.setWindowTitle(u'验证失败')
            # message.setIcon(QtGui.QMessageBox.Warning)
            # message.addButton(u'确定', QtGui.QMessageBox.AcceptRole)
            # message.exec_()
            QtGui.QMessageBox.warning(self, u'验证失败', err_msg)
