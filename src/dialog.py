# gui imports
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import QFile, QObject, Slot


# nebula imports
from nebula.auth import user
from nebula.common import gui
reload(gui)

# python imports
import os
import sys


# construct commonly used paths
rootPath = os.path.dirname(os.path.dirname(__file__))
uiPath = os.path.join(rootPath, 'ui')
iconPath = os.path.join(rootPath, 'icons')

class Dialog(QObject):
    def __init__(self, parent=gui.getMayaWindow()):
        # get the ui form
        super(Dialog, self).__init__(parent)
        self.form = gui.getUiForm(os.path.join(uiPath, 'dialog.ui'))
        self.username = os.environ['USERNAME']
        self.success = True
        self.setWindowIcon(QIcon(os.path.join(iconPath, 'login.png')))
        self.setUsername()
        self.passwordBox.setFocus()

        # connections
        self.loginButton.clicked.connect(self.login)
        self.cancelButton.clicked.connect(self.closeWindow)

    def __getattr__(self, name):
        return getattr(self.form, name)

    def setUsername(self):
        self.usernameBox.setText(self.username)

    def login(self):
        username = str(self.usernameBox.text())
        password = str(self.passwordBox.text())
        #user.login(username, password)
        try:
            user.login(username, password)
            self.accept()
        except Exception, e:
            gui.showMessage(self, title='Login', msg=str(e))

    def closeWindow(self):
        self.close()
        self.reject()

    def closeEvent(self, event):
        self.deleteLater()
