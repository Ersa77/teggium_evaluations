from PyQt5.QtWidgets import QApplication, QLineEdit, QHeaderView, QTableWidgetItem,QMainWindow, QComboBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from conection import traer_preguntas

class cuestionario(QMainWindow):
    def __init__(self, campaign, analyst, supervisor, siniestro, fecha_evaluacion, proceso_pt, tipo_evaluacion, evaluador, preguntas, desviaciones):
        super().__init__()
        loadUi('interfaces/analista_calidad/cuestionario.ui', self)
        self.usuario_evaluado.setText("Usuario Evaluado: " + analyst)
        self.proceso_evaluado.setText("Proceso Evaluado: " + proceso_pt)
        self.tipo_evaluacion.setText("Tipo de Evaluación: " + tipo_evaluacion)

        self.space_preguntas.setRowCount(len(preguntas))
        self.space_preguntas.setColumnCount(3)
        self.space_preguntas.setHorizontalHeaderItem(0, QTableWidgetItem("Preguntas"))
        self.space_preguntas.setHorizontalHeaderItem(1, QTableWidgetItem(""))
        self.space_preguntas.setHorizontalHeaderItem(2, QTableWidgetItem(""))

        for fila1, pregunta1 in enumerate(preguntas):
                #Se establecen las preguntas en la columna 0
                new_item_row1 = QTableWidgetItem(str(pregunta1[1]) + " (Valor: " +str(pregunta1[2]) + " puntos)")
                self.space_preguntas.setItem(fila1, 0, new_item_row1)

                #Se establece el combobox para SI o NO
                resp1 = QComboBox()
                resp1.addItem("Si")
                resp1.addItem("No")
                resp1.addItem("N/A")
                self.space_preguntas.setCellWidget(fila1, 1, resp1)

                #Se establece el textedit para los comentarios 
                comentarios_preg = QLineEdit()
                comentarios_preg.setPlaceholderText("Comentarios")
                self.space_preguntas.setCellWidget(fila1, 2, comentarios_preg)

        self.space_preguntas.resizeColumnsToContents()
        self.space_preguntas.resizeRowsToContents()
        self.space_preguntas.setColumnWidth(0,800)

        self.space_desviaciones.setRowCount(len(desviaciones))
        self.space_desviaciones.setColumnCount(3)
        self.space_desviaciones.setHorizontalHeaderItem(0, QTableWidgetItem("Desviaciones"))
        self.space_desviaciones.setHorizontalHeaderItem(1, QTableWidgetItem(""))
        self.space_desviaciones.setHorizontalHeaderItem(2, QTableWidgetItem(""))

        for fila2, pregunta2 in enumerate(desviaciones):
                #Se establecen las preguntas en la columna 0
                new_item_row2 = QTableWidgetItem(str(pregunta2[1]))
                self.space_desviaciones.setItem(fila2, 0, new_item_row2)

                #Se establece el combobox para SI o NO
                resp2 = QComboBox()
                resp2.addItem("No")
                resp2.addItem("Si")
                resp2.addItem("N/A")
                self.space_desviaciones.setCellWidget(fila2, 1, resp2)

                #Se establece el textedit para los comentarios 
                comentarios_desv = QLineEdit()
                comentarios_desv.setPlaceholderText("Comentarios")
                self.space_desviaciones.setCellWidget(fila2, 2, comentarios_desv)
        
        self.space_desviaciones.resizeColumnsToContents()
        self.space_desviaciones.resizeRowsToContents()
        self.space_desviaciones.setColumnWidth(0,800)

        self.clear_evaluation.clicked.connect(self.limpiar)
        self.cancel_evaluation.clicked.connect(self.cancelar)
        self.save_evaluation.clicked.connect(lambda: self.guardarEvaluacion(campaign=campaign, analyst=analyst, supervisor=supervisor, siniestro=siniestro, fecha_evaluacion=fecha_evaluacion, proceso_pt=proceso_pt, tipo_evaluacion=tipo_evaluacion, evaluador=evaluador))
        #Se establece el combobox para En tiempo o no
        self.sla.addItem("Dentro")
        self.sla.addItem("Fuera")

    def limpiar(self):
        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCurrentIndex(-1)
        for lineedit in self.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def cancelar(self):
        self.close()

    def guardarEvaluacion(self, **kwargs):
         campaign = kwargs.get("campaign", None)
         analyst = kwargs.get("analyst", None)
         supervisor = kwargs.get("supervisor", None)
         siniestro = kwargs.get("siniestro", None)
         fecha_evaluacion = kwargs.get("fecha_evaluacion", None)
         proceso_pt = kwargs.get("proceso_pt", None)
         tipo_evaluacion = kwargs.get("tipo_evaluacion", None)
         evaluador = kwargs.get("evaluador", None)
         preguntas = traer_preguntas(self, proceso_pt)
         print(analyst, campaign, supervisor, siniestro, fecha_evaluacion, proceso_pt, tipo_evaluacion, evaluador)
         resultado= 0
         for fila, pregunta in enumerate(preguntas):
                #muestra la pregunta (mismo orden en el que las trae, asi que no hay pierde)
                print(str(pregunta[1]) + " (Valor " + str(pregunta[2]) + " puntos)")

                #Se trae el combobox con SI o NO
                res= self.space_preguntas.cellWidget(fila, 1).currentText()
                print(self.space_preguntas.cellWidget(fila, 1).currentText())
                if res == 'Si':
                     resultado= resultado + int(pregunta[2])

                #Se trae el textedit con los comentarios 
                print(self.space_preguntas.cellWidget(fila, 2).text())
         print("RESULTADO DE LA EVALUACION: " + str(resultado))

if __name__ == '__main__':
    app = QApplication([])
    ventana_cuestionario = cuestionario()
    ventana_cuestionario.show()
    app.exec_()