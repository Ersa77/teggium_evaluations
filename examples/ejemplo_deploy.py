from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QDateEdit
from PyQt5.QtCore import QDate

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana Principal')
        self.setGeometry(100, 100, 300, 250)

        self.etiqueta_texto = QLabel('Ingrese un texto:', self)
        self.etiqueta_texto.move(20, 20)

        self.entrada_texto = QLineEdit(self)
        self.entrada_texto.setGeometry(20, 50, 200, 30)

        self.etiqueta_combobox = QLabel('Seleccione una opción:', self)
        self.etiqueta_combobox.move(20, 90)

        self.combobox_opciones = QComboBox(self)
        self.combobox_opciones.setGeometry(20, 120, 200, 30)
        self.combobox_opciones.addItems(['Opción 1', 'Opción 2', 'Opción 3'])

        self.etiqueta_fecha = QLabel('Fecha:', self)
        self.etiqueta_fecha.move(20, 160)

        self.fecha_hoy = QDate.currentDate()
        self.fecha_edit = QDateEdit(self.fecha_hoy, self)
        self.fecha_edit.setGeometry(20, 190, 200, 30)

        self.boton_mostrar_ventana_secundaria = QPushButton('Mostrar Ventana Secundaria', self)
        self.boton_mostrar_ventana_secundaria.setGeometry(20, 230, 200, 30)
        self.boton_mostrar_ventana_secundaria.clicked.connect(self.mostrar_ventana_secundaria)

    def mostrar_ventana_secundaria(self):
        texto_ingresado = self.entrada_texto.text()
        opcion_seleccionada = self.combobox_opciones.currentText()
        fecha_seleccionada = self.fecha_edit.date().toString("dd/MM/yyyy")

        self.ventana_secundaria = VentanaSecundaria(texto_ingresado, opcion_seleccionada, fecha_seleccionada)
        self.ventana_secundaria.show()

class VentanaSecundaria(QMainWindow):
    def __init__(self, texto, opcion, fecha):
        super().__init__()
        self.setWindowTitle('Ventana Secundaria')
        self.setGeometry(200, 200, 300, 200)

        self.layout = QVBoxLayout()

        self.etiqueta_texto = QLabel('Texto ingresado en la ventana principal:', self)
        self.layout.addWidget(self.etiqueta_texto)

        self.etiqueta_texto_ingresado = QLabel(texto, self)
        self.layout.addWidget(self.etiqueta_texto_ingresado)

        self.etiqueta_opcion = QLabel('Opción seleccionada:', self)
        self.layout.addWidget(self.etiqueta_opcion)

        self.etiqueta_opcion_seleccionada = QLabel(opcion, self)
        self.layout.addWidget(self.etiqueta_opcion_seleccionada)

        self.etiqueta_fecha = QLabel('Fecha seleccionada:', self)
        self.layout.addWidget(self.etiqueta_fecha)

        self.etiqueta_fecha_seleccionada = QLabel(fecha, self)
        self.layout.addWidget(self.etiqueta_fecha_seleccionada)

        self.widget_central = QWidget(self)
        self.widget_central.setLayout(self.layout)
        self.setCentralWidget(self.widget_central)

if __name__ == '__main__':
    app = QApplication([])
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    app.exec_()

