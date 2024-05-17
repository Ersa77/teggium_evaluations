from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate
from functools import partial
from conection import *
from PyQt5.QtGui import QIcon
fecha_evaluacion= QDate.currentDate()

#CLASE (VENTANA) PARA NUEVA EVALUACIÓN
class new_evaluation(QMainWindow):

#Funcion para iniciar la interfaz uwu
    def __init__(self):
        super().__init__()
        loadUi('interfaces/analista_calidad/new_evaluation.ui', self)
        self.setWindowIcon(QIcon('media/icons/icon_app.ico'))
        self.setWindowTitle('NUEVA EVALUACION')
        self.evaluation_date.setDate(fecha_evaluacion)
        self.campania.addItem("-Seleccionar-",0)
        self.supervisor.addItem("-Seleccionar-",0)
        self.analyst_name.addItem("-Seleccionar-",0)
        llenar_campaings(self)
        self.campania.currentIndexChanged.connect(self.actualizar_supervisor)
        self.supervisor.currentIndexChanged.connect(self.actualizar_analista)
        #llenar_supervisor(self, campaign)
        llenar_tipos_evaluaciones(self)
        llenar_activity(self)
        llenar_evaluador(self)
        self.clear_form.clicked.connect(self.limpiar)
        self.cancel.clicked.connect(self.cancelar)
        self.go.clicked.connect(self.iniciar)
        
    
#Funciones para los botones uwu
    def limpiar(self):
        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCurrentIndex(-1)
        for lineedit in self.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
        self.evaluation_date.setDate(fecha_evaluacion)

    def cancelar(self):
        self.close()

    def iniciar(self):
        from cuestionario import cuestionario
        campaign = self.campania.currentText()
        analyst= self.analyst_name.currentText()
        supervisor= self.supervisor.currentText()
        siniestro= self.no_siniestro.text()
        fecha_evaluacion= self.evaluation_date.date().toString("dd-MM-yyyy")
        tipo_evaluacion= self.tipo_evaluacion.currentText()
        proceso_pt= self.activity.currentText()
        evaluador= self.analista_calidad.currentText()
        preguntas= traer_preguntas(self,proceso_pt)
        desviaciones= traer_desviaciones(self, proceso_pt)

        self.empezar_cuestionario = cuestionario(campaign, analyst, supervisor, siniestro, fecha_evaluacion, proceso_pt, tipo_evaluacion, evaluador, preguntas, desviaciones)
        self.close()
        self.empezar_cuestionario.show()

#Cuando se cambia un valor de los combobox de campaña o supervisor
    def actualizar_supervisor(self):
        self.supervisor.clear()
        campaign= self.campania.currentText()
        llenar_supervisor(self, campaign)
    
    def actualizar_analista(self):
        self.analyst_name.clear()
        campaign= self.campania.currentText()
        supervisor= self.supervisor.currentText()
        llenar_analistas(self, campaign, supervisor)

if __name__ == "__main__":
    app = QApplication([])
    login_window = new_evaluation()
    login_window.show()
    app.exec_()