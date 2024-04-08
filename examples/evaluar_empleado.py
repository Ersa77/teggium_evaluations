import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi

class ventanaprincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interfaces/form.ui', self)
        #ESTABLECER TITULO PARA LA VENTANA
        self.setWindowTitle("FORMATO DE EVALUACION DE CALIDAD PARA PERDIDAS TOTALES TEGGIUM 2024")
        #LLENAR CAMPAÑAS UWU
        self.campania.clear()
        self.campania.addItems(["",\
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
        self.analyst_name.currentIndexChanged.connect(self.mostrar_seleccion)
        #LLENAR SUPERVISORES
        self.supervisor.clear()
        self.supervisor.addItems(["",\
                                  "Jose de Jesus Guerrero Amador",\
                                  "Maria del Socorro Bello Nicasio",\
                                  "Gloria Yaneli Nuñez Sanchez"])
        self.supervisor.currentIndexChanged.connect(self.mostrar_seleccion)
        #Entrada de numero de siniestro

        #FECHA DE EVALUACIÓN
        fecha_evaluacion= QDate.currentDate()
        self.evaluation_date.setDate(fecha_evaluacion)
        #LLENAR TIPO DE EVALUACION
        self.tipo_evaluacion.clear()
        self.tipo_evaluacion.addItems(["",\
                                       "General",\
                                       "Cero Critico",\
                                       "Cero"])
        self.tipo_evaluacion.currentIndexChanged.connect(self.mostrar_seleccion)
        #LLENAR ACTIVIDADES
        self.activity.clear()
        self.activity.addItems(["",\
                                "Validación Documental De Personas Físicas",\
                                "Validación Documental De Personas Morales", \
                                "Llamadas Primer Contato", \
                                "Llamadas De Seguimiento"])
        self.activity.currentIndexChanged.connect(self.mostrar_seleccion)
        #LLENAR ANALISTAS DE CALIDAD
        self.analista_calidad.clear()
        self.analista_calidad.addItems(["","Andrea Vazquez Vazquez",\
                                            "Victor Leo Orozco"])
        self.analista_calidad.currentIndexChanged.connect(self.mostrar_seleccion)


    def mostrar_seleccion(self,index):
        seleccion= self.campania.itemText(index)
        seleccion= self.analyst_name.itemText(index)
        seleccion= self.supervisor.itemText(index)
        seleccion= self.tipo_evaluacion.itemText(index)
        seleccion= self.activity.itemText(index)
        seleccion= self.analista_calidad.itemText(index)
        #print("Seleccionado: ", seleccion)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaprincipal()
    ventana.show()
    sys.exit(app.exec_())