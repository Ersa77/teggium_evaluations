#Importamos lo que necesitamos para trabajar:
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QStandardItemModel, QIcon, QStandardItem
from PyQt5.uic import loadUi
from conection import visualizarUsuario, promedioUsuario, numEvaluacionesUser, listadoEvaluacionesUser, promedioEvaEspecifica, mostrarEvasPorUsuario, retroalimentacion

#Creamos la clase principal del dash individual para llamarla desde la pagina principa, del sistema
class dashUser(QWidget):
    #Funcion principal para inicializar la clase principal, es como si el class fuera el cuerpo, y esta funcion el alma, o lo que lo haga vivir
    def __init__(self):
        super().__init__()
        #Cargar nuestro formulario
        loadUi('interfaces/analista_calidad/show_analyst_data.ui', self)
        self.setWindowIcon(QIcon('media/icons/icon_app.ico'))
        self.setWindowTitle('DESEMPEÑO POR EJECUTIVO')
        #llenar combobox de usuarios
        visualizarUsuario(self)
        #Cuando se cambie el combobox de usuario, actualizar el promedio, cantidad de evaluaciones y el llenado del filtro de siniestros
        self.userFilter.currentIndexChanged.connect(self.promedioUsuario)
        self.userFilter.currentIndexChanged.connect(self.cantidadEvas)
        self.userFilter.currentIndexChanged.connect(self.siniestrosEvaluados)
        #Cuando cambie el combobox de los siniestros por usuario, actualizar el promedio de dicho siniestro, las tabla de respuestas y el texto de retroaliemttacion
        self.siniestroFilter.currentIndexChanged.connect(self.promedioEva)
        self.siniestroFilter.currentIndexChanged.connect(self.respuestasEva)
        self.siniestroFilter.currentIndexChanged.connect(self.retroUsuario)
        #Salir y volver a la pagina principal
        self.exit.clicked.connect(self.salir)

    #Creamos las funciones para asignarlas al llenado de comboboxes, botones, labels:
    #Esto lo manejo asi mas que nada para que se vallan cambiando segun lo requiera, pro ejemplo si cambio un combobox que se actualicen los demas
    #Es decir, que se vallan mandando llamar segun se requiera, y en el evento que se requiera
    #Empezamos con la funcion para traer el promedio general
    def promedioUsuario(self):
        usuario= self.userFilter.currentText()
        promUsuario= promedioUsuario(self, usuario)
        self.promedioUser.setText("PROMEDIO GENERAL: " + str(round(promUsuario,2)))
    # Funcion para traer la cantidad de evaluaciones
    def cantidadEvas(self):
        usuario= self.userFilter.currentText()
        cantidadEvas = numEvaluacionesUser(self,usuario)
        self.evaluaciones.setText("EVALUACIONES: " + str(cantidadEvas))
    # Funcion para llenar el filtro de siniestros segun el usuario seleccionado
    def siniestrosEvaluados(self):
        self.siniestroFilter.clear()
        usuario= self.userFilter.currentText()
        listadoEvaluacionesUser(self, usuario)
    # Funcion para traer el promedio del siniestro seleccionado
    def promedioEva(self):
        usuario= self.userFilter.currentText()
        siniestro= self.siniestroFilter.currentText()
        promedioEva = promedioEvaEspecifica(self, usuario, siniestro)
        self.promedioEvaluacion.setText("RESULTADO: " + str(promedioEva))
    # Funcion para traer las preguntas de la evaluacion del siniestro seleccionado (misma dinamica que en el dash, se establece un modelo y se le asigna a la tabla)
    def respuestasEva(self):
        usuario= self.userFilter.currentText()
        siniestro= self.siniestroFilter.currentText()
        respuestas= mostrarEvasPorUsuario(self, usuario, siniestro)
        if len(respuestas) == 0:
            modelRespuestas = QStandardItemModel(len(respuestas),1)
            headerRespuestas = ['NOT DATA AVAILABLE | NADA QUE VER POR ACA UWU']
            modelRespuestas.setHorizontalHeaderLabels(headerRespuestas)
            self.listaEvaluaciones.setModel(modelRespuestas)
            self.listaEvaluaciones.resizeColumnsToContents()
        else:
            modelRespuestas = QStandardItemModel(len(respuestas), len(respuestas[1]))
            headerRespuestas = ['PREGUNTA', 'RESPUESTA']
            modelRespuestas.setHorizontalHeaderLabels(headerRespuestas)
            for respuesta, dataRespuesta in enumerate(respuestas):
                for columnaRespuesta, datacolumnaRespuesta in enumerate(dataRespuesta):
                    itemRespuesta = QStandardItem(str(datacolumnaRespuesta))
                    modelRespuestas.setItem(respuesta, columnaRespuesta, itemRespuesta)
            self.listaEvaluaciones.setModel(modelRespuestas)
            self.listaEvaluaciones.resizeColumnsToContents()
    # Funcion para llenar el texto de retroalimentación
    def retroUsuario(self):
        self.retro.setText('')
        usuario= self.userFilter.currentText()
        siniestro= self.siniestroFilter.currentText()
        comentarios = retroalimentacion(self, usuario, siniestro)
        if len(comentarios) == 0:
            self.retro.setText("Todo en orden, ¡sigue así!")
        else:
            retroUser = "RETROALIMENTACION \n\n"
            for comentario in comentarios:
                retroUser += comentario[0] + ': ' + comentario[1] +'\n\n'
            self.retro.setText(retroUser)
            self.retro.setWordWrap(True)
    #Funcion para salir
    def salir(self):
        self.close()


#Lo de ley, es como el "Arrancar"
if __name__ == '__main__':
    app = QApplication([])
    dashUsuario= dashUser()
    dashUsuario.show()
    app.exec_()