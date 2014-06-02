try:
    from uiContainer import uic
except:
    from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
parent = None
try:
    import qtify_maya_window as qtfy
    parent = qtfy.getMayaWindow()
except:
    pass
from customui import ui as cui
import auth.user as user

import os
import os.path as osp
import sys

rootPath = osp.dirname(osp.dirname(__file__))
uiPath = osp.join(rootPath, 'ui')
iconPath = osp.join(rootPath, 'icons')

Form, Base = uic.loadUiType(osp.join(uiPath, 'dialog.ui'))
class Dialog(Form, Base):

    def __init__(self, parent=parent):
        super(Dialog, self).__init__(parent)
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
        #user.login(username, password)
        try:
            user.login(username, password)
            self.accept()
        except:
            cui.showMessage(self, title='Login', msg='Invalid Password/Username combination')
        
    def closeWindow(self):
        self.close()
        self.reject()
        self.deleteLater()