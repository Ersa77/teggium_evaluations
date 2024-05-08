from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class Logout(QWidget):
    def __init__(self, usuario, rol):
        super().__init__()
        loadUi("interfaces/analista_calidad/mainpage_analista_calidad.ui", self)
        self.setWindowTitle('PAGINA PRINCIPAL')
        self.welcome_label_analista_calidad.setText('BIENVENID@\n'+ usuario + '\n' + rol)
        self.new_evaluation.clicked.connect(self.add_evaluation)
        self.retro.clicked.connect(self.showRetro)
        self.muestreo.clicked.connect(self.en_construccion)
        self.openDash.clicked.connect(self.showDash)
        self.logout_button.clicked.connect(self.logout)

    def logout(self):
        self.close()
        from log_in import Login
        self.login_window = Login()
        self.login_window.show()

    def add_evaluation(self):
        from new_evaluation import new_evaluation
        self.nueva_evaluacion = new_evaluation()
        self.nueva_evaluacion.show()
    
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
