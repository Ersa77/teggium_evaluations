from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.uic import loadUi
from conection import traerPromedios, traerPromedioGeneral, traerTotalEvaluaciones, traerTotalCeros, llenarFiltros, traerErrores, traerGraves

class dashBoard(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('interfaces/analista_calidad/dash.ui', self)
        #Esto es para QTablesView, supongo que es diferente a trabajar con QTableWidget: HACER LO MISMO PARA LAS DEMAS TABLAS XD (o no uwu)
        rowsPromedios = traerPromedios(self)
        #Para QTableView se crea un modelo de datos:
        modelPromedios = QStandardItemModel(len(rowsPromedios), len(rowsPromedios[0]))
        #Se establecen los encabezados y se setean en la tabla:
        headersPromedios = ['USUARIO','ACTIVIDAD', 'PROMEDIO']
        modelPromedios.setHorizontalHeaderLabels(headersPromedios)
        #Se llena la tabla con el resultado de la consulta
        for rowPromedios, row_dataPromedios in enumerate(rowsPromedios):
            for columnPromedios, dataPromedios in enumerate(row_dataPromedios):
                itemPromedios = QStandardItem(str(dataPromedios))
                modelPromedios.setItem(rowPromedios, columnPromedios, itemPromedios)
        #Se establece el modelo en la tabla
        self.usuariosPromedios.setModel(modelPromedios)
        #Se ajusta el ancho de las columnas
        self.usuariosPromedios.resizeColumnsToContents()

        #setear promedio general, conteo de evaluaciones y ceros:
        promedioGral = traerPromedioGeneral(self)
        self.promedioGeneral.setText('PROMEDIO GENERAL: ' + str(round(promedioGral,2)))
        #setear promedio general, conteo de evaluaciones y ceros:
        evaluaciones = traerTotalEvaluaciones(self)
        self.totalEvaluaciones.setText('TOTAL EVALUACIONES: ' + str(evaluaciones))
        #setear promedio general, conteo de evaluaciones y ceros:
        ceros = traerTotalCeros(self)
        self.totalCeros.setText('TOTAL CEROS: ' + str(ceros))

        #FITROS:
        llenarFiltros(self)
        #CONSULTA
        

if __name__ == '__main__':
    app = QApplication([])
    ventanaDash= dashBoard()
    ventanaDash.show()
    app.exec_()