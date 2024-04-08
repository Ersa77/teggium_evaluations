from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sqlite3

class Login(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/log_in.ui", self)
        self.setWindowTitle('INICIAR SESION')
        self.log_in_button.clicked.connect(self.login)

    def login(self):
        username = self.username.text()
        password = self.userpass.text()  # Usar text() para obtener el texto del campo de contraseña

        from conection import crear_conexion
        conexion = crear_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM auditores_calidad WHERE username=? AND pass=?", (username, password))
        usuario = cursor.fetchone()

        if not username.strip() or not password.strip():
            QMessageBox.warning(self, "INICIO DE SESION", "POR FAVOR LLENE LOS CAMPOS")
        
        elif usuario:
            from mainpage_analista_calidad import Logout
            self.close()
            QMessageBox.information(self, "INICIO DE SESION", "INICIO DE SESION EXITOSO")
            self.main_window= Logout()
            self.main_window.show()
            self.log_in = Login()
        
        else:
            QMessageBox.warning(self, "INICIO DE SESION", "CREDENCIALES INCORRECTAS")

if __name__ == "__main__":
    app = QApplication([])
    login_window = Login()
    login_window.show()
    app.exec_()

        