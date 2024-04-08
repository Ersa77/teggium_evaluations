from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
#import sqlite3

class Logout(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/analista_calidad/mainpage_analista_calidad.ui", self)
        self.setWindowTitle('PAGINA PRINCIPAL')
        self.logout_button.clicked.connect(self.logout)

    def logout(self):
        self.close()
        from log_in import Login
        self.login_window = Login()
        self.login_window.show()

if __name__ == "__main__":
    app = QApplication([])
    login_window = Logout()
    login_window.show()
    app.exec_()
