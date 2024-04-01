import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi

class ventanaprincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('form.ui', self)
        #LLENAR CAMPAÑAS UWU
        self.campania.clear()
        self.campania.addItems(["",\
                                "AFIRME",\
                                "GNP",\
                                "AXA",\
                                "HDI"])
        self.campania.currentIndexChanged.connect(self.mostrar_seleccion)
        #LLENAR EMPLEADOS
        self.analyst_name.clear()
        self.analyst_name.addItems(["","Nombre1",\
                                    "Nombre2", \
                                    "Nombre3", \
                                    "Nombre4",\
                                    "Nombre5",\
                                    "Nombre6"])
        self.campania.currentIndexChanged.connect(self.mostrar_seleccion)
        #LLENAR ACTIVIDADES
        self.activity_2.clear()
        self.activity_2.addItems(["",\
                                "Validación Documental De Personas Físicas",\
                                "Validación Documental De Personas Morales", \
                                "Llamadas Primer Contato", \
                                "Llamadas De Seguimiento"])
        self.activity_2.currentIndexChanged.connect(self.mostrar_seleccion)
        #LLENAR ANALISTAS DE CALIDAD
        self.analista_calidad.clear()
        self.analista_calidad.addItems(["","Andrea Vazquez Vazquez",\
                                            "Victor Leo Orozco"])
        self.analista_calidad.currentIndexChanged.connect(self.mostrar_seleccion)
        #FECHA DE EVALUACIÓN
        fecha_evaluacion= QDate.currentDate()
        self.evaluation_date.setDate(fecha_evaluacion)


    def mostrar_seleccion(self,index):
        seleccion= self.campania.itemText(index)
        seleccion= self.analyst_name.itemText(index)
        seleccion= self.activity_2.itemText(index)
        seleccion= self.analista_calidad.itemText(index)
        #print("Seleccionado: ", seleccion)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaprincipal()
    ventana.show()
    sys.exit(app.exec_())