import site
site.addsitedir(r"R:\Pipe_Repo\Users\Qurban\utilities")
from uiContainer import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt

site.addsitedir(r"R:\Pipe_Repo\Users\Hussain\packages")
import qtify_maya_window as qtfy

import os
import os.path as osp
import sys

rootPath = osp.dirname(osp.dirname(__file__))
uiPath = osp.join(rootPath, 'ui')
iconPath = osp.join(rootPath, 'icons')

Form, Base = uic.loadUiType(osp.join(uiPath, 'window.ui'))
class Window(Form, Base):

    def __init__(self, parent=qtfy.getMayaWindow()):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        
        self.setWindowIcon(QIcon(osp.join(iconPath, 'login.png')))
        
        self.loginButton.clicked.connect(self.login)
        self.cancelButton.clicked.connect(self.close)
        
        self.setUsername()
        
    def setUsername(self):
        username = os.environ.get('USERNAME')
        self.usernameBox.setText(username)
        
    def login(self):
        password = str(self.passwordBox.text())
        print password
        self.close()