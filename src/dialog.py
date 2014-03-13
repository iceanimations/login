from uiContainer import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import qtify_maya_window as qtfy

import auth.user as user

import os
import os.path as osp
import sys
import pymel.core as pc

rootPath = osp.dirname(osp.dirname(__file__))
uiPath = osp.join(rootPath, 'ui')
iconPath = osp.join(rootPath, 'icons')

Form, Base = uic.loadUiType(osp.join(uiPath, 'window.ui'))
class Window(Form, Base):

    def __init__(self, parent=qtfy.getMayaWindow()):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.username = os.environ['USERNAME']
        self.success = True
        
        self.setWindowIcon(QIcon(osp.join(iconPath, 'login.png')))
        
        self.loginButton.clicked.connect(self.login)
        self.cancelButton.clicked.connect(self.closeWindow)
        
        self.setUsername()
        self.passwordBox.setFocus()
        
    def setUsername(self):
        self.usernameBox.setText(self.username)
        
    def login(self):
        username = str(self.usernameBox.text())
        password = str(self.passwordBox.text())
        try:
            user.login(username, password)
            self.accept()
        except:
            pc.warning('Invalid password')
        
    def closeWindow(self):
        self.close()
        self.reject()
        self.deleteLater()