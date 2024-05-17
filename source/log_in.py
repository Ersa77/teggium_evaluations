from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon

class Login(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/log_in.ui", self)
        self.setWindowIcon(QIcon('media/icons/icon_app.ico'))
        self.setWindowTitle('INICIAR SESION')
        self.log_in_button.clicked.connect(self.login)
        self.show_pass.stateChanged.connect(self.show_pass_uwu)
        self.userpass.setEchoMode(QLineEdit.Password)
        self.cerrar_button.clicked.connect(self.cerrar)

    def show_pass_uwu(self, state):
        if state == 2:  
            self.userpass.setEchoMode(QLineEdit.Normal)
        else:
            self.userpass.setEchoMode(QLineEdit.Password)

    def login(self):
        username = self.username.text()
        password = self.userpass.text()  

        from conection import crear_conexion
        conexion = crear_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM auditores_calidad WHERE username=? AND pass=?", (username, password))
        usuario = cursor.fetchone()

        if not username.strip() or not password.strip():
            QMessageBox.warning(self, "INICIO DE SESION", "POR FAVOR LLENE LOS CAMPOS")
        
        elif usuario:
            from mainpage_analista_calidad import Logout
            from conection import usuario_analista_evaluador
            self.close()
            QMessageBox.information(self, "INICIO DE SESION", "INICIO DE SESION EXITOSO")
            usuario_logeado = usuario_analista_evaluador(username)
            nombre, rol = usuario_logeado
            self.main_window= Logout(nombre, rol)
            self.main_window.show()
            self.log_in = Login()
        
        else:
            QMessageBox.warning(self, "INICIO DE SESION", "CREDENCIALES INCORRECTAS")


    def cerrar(self):
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    login_window = Login()
    login_window.show()
    app.exec_()

        