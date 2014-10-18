#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-10-16 23:43:26
# @Author  : jphome (jphome98@163.com)
# @Link    : http://jphome.github.com
# @Version : $Id$

import sys
from PyQt4 import QtCore,  QtGui

from ui import *
from util import *

userinfo = user_info.UserInfo() 
userpair = {}
for key in userinfo.dict_userinfo.keys():
    pair = key.split(':')
    # print pair
    userpair[pair[0]] = pair[1]

def login():
    # authpair = {'admin':'1234'}
    login = E_Ui_login.LoginDialog(authpair=userpair)
    ret = login.exec_()
    print "ret: ", ret
    if ret:
        return True
    return False

def main():
    app = QtGui.QApplication(sys.argv)
    if login():
        win = QtGui.QMainWindow()
        ui = Ui_mainwindow.Ui_MainWindow()
        ui.setupUi(win)
        win.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    # print userinfo.dict_userinfo
