# -*- coding: utf-8 -*-

"""
Module implementing LoginDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_login import Ui_LoginDialog

class LoginDialog(QDialog, Ui_LoginDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        if unicode(self.username.text()) == u'admin' and unicode(self.password.text()) == u'12345':
            self.accept()
        else:
            # QtGui.QMessageBox.critical(self, 'Error', 'User name or password error')
            self.reject()
