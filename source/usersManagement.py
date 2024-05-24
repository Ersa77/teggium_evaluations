from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtGui import QIcon

class manageUsers(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('interfaces/analista_calidad/createUser.ui',self)
        self.setWindowIcon(QIcon('media/icons/icon_app.ico'))
        self.setWindowTitle('CONFIGURACION DEL SISTEMA')
        self.exitButton.clicked.connect(self.closeUsersManagement)

    def closeUsersManagement(self):
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    usersManagementWindow= manageUsers()
    usersManagementWindow.show()
    app.exec_()

