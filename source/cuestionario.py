from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QMainWindow, QComboBox, QTextEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from conection import traer_preguntas

class cuestionario(QMainWindow):
    def __init__(self, evaluado, proceso_pt, tipo_evaluacion, resultados):
        super().__init__()
        loadUi('interfaces/analista_calidad/cuestionario.ui', self)
        self.usuario_evaluado.setText("Usuario Evaluado: " + evaluado)
        self.proceso_evaluado.setText("Proceso Evaluado: " + proceso_pt)
        self.tipo_evaluacion.setText("Tipo de Evaluación: " + tipo_evaluacion)
        pos_a= 130
        for pregunta in resultados:
            new_label= QLabel(self)
            new_label.setText(pregunta[0])
            new_label.setAlignment(Qt.AlignLeft)
            new_label.adjustSize()
            new_label.move(30, pos_a)
            pos_a += new_label.height()+5


if __name__ == '__main__':
    app = QApplication([])
    ventana_cuestionario = cuestionario()
    ventana_cuestionario.show()
    app.exec_()