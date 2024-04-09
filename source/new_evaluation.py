from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate
fecha_evaluacion= QDate.currentDate()

class new_evaluation(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interfaces/analista_calidad/new_evaluation.ui', self)
        self.clear_form.clicked.connect(self.limpiar)
        self.cancel.clicked.connect(self.cancelar)
        self.evaluation_date.setDate(fecha_evaluacion)

    def limpiar(self):
        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCurrentIndex(-1)
        for lineedit in self.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
        self.evaluation_date.setDate(fecha_evaluacion)

    def cancelar(self):
        self.close()

    #Aqui va la de continuar buajajaja

if __name__ == "__main__":
    app = QApplication([])
    login_window = new_evaluation()
    login_window.show()
    app.exec_()