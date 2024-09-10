from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon

class Logout(QWidget):
    def __init__(self, usuario, rol):
        super().__init__()
        loadUi("interfaces/supervisor/mainpageSupervisor.ui", self)
        self.setWindowIcon(QIcon('media/icons/icon_app.ico'))
        self.setWindowTitle('PAGINA PRINCIPAL')
        self.labelSupervisor.setText('BIENVENID@\n'+ usuario + '\n' + rol)
        self.retro.clicked.connect(self.showRetro)
        self.openDash.clicked.connect(self.showDash)
        self.logout_button.clicked.connect(self.logout)

    def logout(self):
        self.close()
        from log_in import Login
        self.login_window = Login()
        self.login_window.show()
    
    def showRetro(self):
        from showAnalystData import dashUser
        self.dashUsuarios = dashUser()
        self.dashUsuarios.show()
    
    def showDash(self):
        from showDash import dashBoard
        self.dashboardo = dashBoard()
        self.dashboardo.show()
    
    def en_construccion(self):
        QMessageBox.information(self,"OPCION", "NO DISPONIBLE TEMPORALMENTE :D")

if __name__ == "__main__":
    app = QApplication([])
    login_window = Logout()
    login_window.show()
    app.exec_()