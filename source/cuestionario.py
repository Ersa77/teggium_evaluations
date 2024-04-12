from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QTableWidgetItem,QMainWindow, QComboBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from conection import traer_preguntas

class cuestionario(QMainWindow):
    def __init__(self, evaluado, proceso_pt, tipo_evaluacion, resultados):
        super().__init__()
        loadUi('interfaces/analista_calidad/cuestionario.ui', self)
        self.usuario_evaluado.setText("Usuario Evaluado: " + evaluado)
        self.proceso_evaluado.setText("Proceso Evaluado: " + proceso_pt)
        self.tipo_evaluacion.setText("Tipo de Evaluación: " + tipo_evaluacion)
        self.space_preguntas.setRowCount(len(resultados))
        self.space_preguntas.setColumnCount(3)
        self.space_preguntas.setHorizontalHeaderItem(0, QTableWidgetItem("Preguntas"))
        self.clear_evaluation.clicked.connect(self.limpiar)
        self.cancel_evaluation.clicked.connect(self.cancelar)
        #Se establece el combobox para En tiempo o no
        self.sla.addItem("Dentro")
        self.sla.addItem("Fuera")

        for fila, pregunta in enumerate(resultados):
                #Se establecen las preguntas en la columna 0
                new_item_row1 = QTableWidgetItem(str(pregunta[1]) + " (Valor: " +str(pregunta[2]) + " puntos)")
                self.space_preguntas.setItem(fila, 0, new_item_row1)

                #Se establece el combobox para SI o NO
                resp1 = QComboBox()
                resp1.addItem("Si")
                resp1.addItem("No")
                resp1.addItem("N/A")
                self.space_preguntas.setCellWidget(fila, 1, resp1)

                #Se establece el textedit para los comentarios 
                comentarios = QLineEdit()
                comentarios.setPlaceholderText("Comentarios")
                self.space_preguntas.setCellWidget(fila, 2, comentarios)

        self.space_preguntas.resizeColumnsToContents()
        self.space_preguntas.resizeRowsToContents()


    def limpiar(self):
        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCurrentIndex(-1)
        for lineedit in self.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def cancelar(self):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    ventana_cuestionario = cuestionario()
    ventana_cuestionario.show()
    app.exec_()