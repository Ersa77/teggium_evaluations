#Primero importamos las librerias a utilizar (sinceramente las fui importando conforme las fui necesitando XD)
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.uic import loadUi
from conection import traerPromedios, traerPromedioGeneral, traerTotalEvaluaciones, traerTotalCeros, llenarFiltros, traerErrores, traerGraves, traerPromedioMensual

#Creamos la clase main para llamarla desde la pagina principal de nuestro programa
class dashBoard(QWidget):
    #Iniciamos la función principal que despliega la interfaz
    def __init__(self):
        super().__init__()
        #Cargamos nuestro formulario
        loadUi('interfaces/analista_calidad/dash.ui', self)
        self.setWindowIcon(QIcon('media/icons/icon_app.ico'))
        self.setWindowTitle('DESEMPEÑO GENERAL')

        #Asignar la función para salir al boton de SALIR
        self.exit.clicked.connect(self.closeDash)
        #Ejecutar la consulta segun el proceso cada vez que cambie el valor del combobox
        self.filtroProceso.currentIndexChanged.connect(self.filtrarProceso)

        #Esto es para QTablesView, supongo que es diferente a trabajar con QTableWidget, empezamos guardando el resultado de la consulta para los promedios en una varaiable 
        rowsPromedios = traerPromedios(self)
        #Para QTableView se crea un modelo de datos:
        modelPromedios = QStandardItemModel(len(rowsPromedios), len(rowsPromedios[0]))
        #Se establecen los encabezados y se setean en la tabla:
        headersPromedios = ['USUARIO','ACTIVIDAD', 'PROMEDIO']
        modelPromedios.setHorizontalHeaderLabels(headersPromedios)
        #Estas son meramente labels, podemos usar la consulta una sola vez y traer la columna que necesitemos
        #Llamamos a la función para setear promedio general, conteo de evaluaciones y ceros:
        promedioGral = traerPromedioGeneral(self)
        self.promedioGeneral.setText('PROMEDIO GENERAL: ' + str(round(promedioGral,2)))
        #Traer promedio mensual:
        promedioMensual = traerPromedioMensual(self)
        self.promedioMensual.setText('PROMEDIO DEL MES: ' + str(round(promedioMensual,2)))
        #setear promedio general, conteo de evaluaciones y ceros:
        evaluaciones = traerTotalEvaluaciones(self)
        self.totalEvaluaciones.setText('TOTAL EVALUACIONES: ' + str(evaluaciones))
        #setear promedio general, conteo de evaluaciones y ceros:
        ceros = traerTotalCeros(self)
        self.totalCeros.setText('TOTAL CEROS: ' + str(ceros))
        #Se llena la tabla con el resultado de la consulta, este for llena cada fila
        for rowPromedios, row_dataPromedios in enumerate(rowsPromedios):
            #Y este for llena cada columna de la fila
            for columnPromedios, dataPromedios in enumerate(row_dataPromedios):
                #Aqui, item promedios va tomandoel valor de cada celda de la tabla resultante de la consulta empezando por el nombre, activiada y promedio, y asi para cada fila
                itemPromedios = QStandardItem(str(dataPromedios))
                #Luego, vamos seteando el valor de itemPromedios en cada posicion de nuestra QTableView, indicando: fila, columna y el valor que se le pondrá, osea itemPromedios
                #el valor de rowPromedios y columnPromedios ira variando segun el ciclo en el que valla
                modelPromedios.setItem(rowPromedios, columnPromedios, itemPromedios)
        #Se establece el modelo en la tabla
        self.usuariosPromedios.setModel(modelPromedios)
        #Se ajusta el ancho de las columnas
        self.usuariosPromedios.resizeColumnsToContents()

        #FITROS:
        llenarFiltros(self)
    
    #Hacemos una funcion para llamar a la consulta
    def filtrarProceso(self):
        #Hacemos el mismo porcedimiento para llenar las tablas de desviaciones graves y errores operativos:
        #Aqui nos pide un parametro extra para la funcion que trae la consulta, en este caso es el proceso que estamos visualizando, entonces asignamos el valor actual del combobox del filtro
        proceso_pt = self.filtroProceso.currentText()
        #Y aplicamos lo mismo que en la tabla promedios, asignamos a una variable el resultado de la funcion
        rowsErrores = traerErrores(self, proceso_pt)    
        #Este if sirve para cuando no haya resultados en la consulta, es decir, cuando no haya errores o desviaciones para mostrar, esto porque necesitamos minimo una fila, si no arroja error
        if len(rowsErrores) == 0:
            #Se establecen los encabezados y se setean en la tabla, si no hay filas resultantes, solo se setea
            #el encabezado indicando que no hay incidencias
            modelErrores = QStandardItemModel(len(rowsErrores),1)
            headersErrores = ['No hay incidencias :D']
            modelErrores.setHorizontalHeaderLabels(headersErrores)
            self.erroresOperativos.setModel(modelErrores)
            self.erroresOperativos.resizeColumnsToContents()
        #En caso de que si haya filas en la consulta, damos formato a la tabla para mostrar los resultados
        else:
            #De igual forma, hacemos un modelo para la QTableView y mnismo proceso que usamos en la tabla de promedios:
            modelErrores = QStandardItemModel(len(rowsErrores), len(rowsErrores[0]))
            #Seteamos 2 encabezados
            headersErrores = ['CASO','# DE INCIDENCIAS']
            #Asignamos los encabezados al modelo de la tabla
            modelErrores.setHorizontalHeaderLabels(headersErrores)
            #Se llena la tabla con el resultado de la consulta
            for rowErrores, row_dataErrores in enumerate(rowsErrores):
                for columnErrores, dataErrores in enumerate(row_dataErrores):
                    itemPromedios = QStandardItem(str(dataErrores))
                    modelErrores.setItem(rowErrores, columnErrores, itemPromedios)
            #Se establece el modelo en la tabla
            self.erroresOperativos.setModel(modelErrores)
            #Se ajusta el ancho de las columnas
            self.erroresOperativos.resizeColumnsToContents()
        #Y los mismo para la tabla de desviaciones graves
        rowsGraves = traerGraves(self, proceso_pt)    
        if len(rowsGraves) == 0:
            #Se establecen los encabezados y se setean en la tabla, si no hay filas resultantes, solo se setea
            #el encabezado indicando que no hay incidencias
            modelGraves = QStandardItemModel(len(rowsGraves),1)
            headersGraves = ['No hay incidencias :D']
            modelGraves.setHorizontalHeaderLabels(headersGraves)
            self.desviacionesGraves.setModel(modelGraves)
            self.desviacionesGraves.resizeColumnsToContents()
        else:
            modelGraves = QStandardItemModel(len(rowsGraves), len(rowsGraves[0]))
            headersGraves = ['CASO','# DE INCIDENCIAS']
            modelGraves.setHorizontalHeaderLabels(headersGraves)
            #Se llena la tabla con el resultado de la consulta
            for rowErrores, row_dataErrores in enumerate(rowsGraves):
                for columnErrores, dataErrores in enumerate(row_dataErrores):
                    itemPromedios = QStandardItem(str(dataErrores))
                    modelGraves.setItem(rowErrores, columnErrores, itemPromedios)
            #Se establece el modelo en la tabla
            self.desviacionesGraves.setModel(modelGraves)
            #Se ajusta el ancho de las columnas
            self.desviacionesGraves.resizeColumnsToContents()
    
    #Esta funcion es para cerrar la ventana del dashboard
    def closeDash(self):
        self.close()

if __name__ == '__main__':
    app = QApplication([])
    ventanaDash= dashBoard()
    ventanaDash.show()
    app.exec_()