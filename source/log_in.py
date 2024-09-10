#ESTA SERÁ LA VENTANA PRINCIPAL DEL SISTEMA, ANTES DE LLEGAR A CUALQUIER OTRA VENTANA HAY QUE PASAR POR AQU
#ESTE SCRIPT ES EL QUE SE EXPORTO A .EXE PARA SER APLICACION DE ESCRITORIO

#Comenzamos trayendo las librerías necesarias
from PyQt5.uic import loadUi #Esta es para cargar los formularios hechos en QT Designer
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit #Esto es para insertar ciertos objetos en la interfaz
from PyQt5.QtGui import QIcon #Esto es meramente estilo de la aplicación, es para que se le establezca un icono bonis XD

#Declaramos la clase main de nuestro ejecutable, esta clase será la encargada de darle vida a la interfaz
class Login(QWidget):
    #Esta función estará en todas las clases main, ya que es la que lo inicializa y carga el formulario
    def __init__(self):
        super().__init__() #Inicializa la clase
        loadUi("interfaces/log_in.ui", self) #Carga el formulario
        self.setWindowIcon(QIcon('media/icons/icon_app.ico'))   #Establece el icono de las ventanas
        self.setWindowTitle('INICIAR SESION')   #Setea el titulo de la ventana
        self.log_in_button.clicked.connect(self.login)  #Asigna la función login al boton log_in_button del formulario
        self.show_pass.stateChanged.connect(self.show_pass_uwu) #Asigna la función para mostrar la contraseña cuando se habilite el checkbox
        self.userpass.setEchoMode(QLineEdit.Password) #Oculta la contraseña por default
        self.cerrar_button.clicked.connect(self.cerrar) #Salir del sistema

#Función para mostrar contraseña
    def show_pass_uwu(self, state): #Se toman como entradas el formulario y el estado del checkbox
        if state == 2:  #Si el checkbox esta habilitado, (estado 2) se muestra la contraseña
            self.userpass.setEchoMode(QLineEdit.Normal)
        else: # Si el checkbox esta deshabilitado (otro estado que no sea 2)
            self.userpass.setEchoMode(QLineEdit.Password)

#Funcion para validar el inicio de sesión
    def login(self):
        #Guardamos la información contenida en los campos usuario y contraseña
        username = self.username.text() 
        password = self.userpass.text()  
        #Importamos la conexión de nuestro archivo y creamos un cursor para ejecutar una consulta
        from conection import crear_conexion
        conexion = crear_conexion()
        cursor = conexion.cursor()
        
        #Usando el cursor anterior hacemos la consulta si el usuario y contraseña existen en la BD
        cursor.execute("SELECT * FROM auditores_calidad WHERE username=? AND pass=?", (username, password))
        usuario = cursor.fetchone()
        
        #Si no se llenó alguno de los campos lanza una advertencia
        if not username.strip() or not password.strip():
            QMessageBox.warning(self, "INICIO DE SESION", "POR FAVOR LLENE LOS CAMPOS")
        
        #Si el usuario y contraseña son correctos, se inicia sesión, y se guardan los datos del usuario logeado para la ventana principal
        elif usuario:
            #AQUI ME QUEDE; HAY QUE ACOMODAR LOS ROLES Y USUARIOS XD (SI HOY HOY XD)
            #Entonces, si el rol es diferente al supervisor, se mete a la pagina normal xd
            from conection import usuario_analista_evaluador
            usuario_logeado = usuario_analista_evaluador(username)
            nombre, rol = usuario_logeado
            if rol != 'Supervisor':  
                from mainpage_analista_calidad import Logout
                self.close()
                QMessageBox.information(self, "INICIO DE SESION", "INICIO DE SESION EXITOSO")
                self.main_window = Logout(nombre, rol)
                self.main_window.show()
                self.log_in = Login()
            else:
                from mainPageSupervisor import Logout
                self.close()
                QMessageBox.information(self, "INICIO DE SESION", "INICIO DE SESION EXITOSO")
                self.main_window = Logout(nombre, rol)
                self.main_window.show()
                self.log_in = Login()
        
        #Si la información ingresada fue incorrecta, se lanza una advertencia
        else:
            QMessageBox.warning(self, "INICIO DE SESION", "CREDENCIALES INCORRECTAS")

#Función para cerrar
    def cerrar(self):
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    login_window = Login()
    login_window.show()
    app.exec_()

        