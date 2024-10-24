#Importamos lo que necesitamos para trabajar:
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QIcon, QStandardItem
from PyQt5.uic import loadUi
from conection import visualizarUsuario, promedioUsuario, numEvaluacionesUser, listadoEvaluacionesUser, promedioEvaEspecifica, mostrarEvasPorUsuario, retroalimentacion, proceso, auditora, supervisor, fechaEva
import openpyxl
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from openpyxl.styles import Alignment
from datetime import datetime

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
        self.siniestroFilter.currentIndexChanged.connect(self.procesoEva)
        self.siniestroFilter.currentIndexChanged.connect(self.fechaEvaluacion)
        #GUARDAR RETRO SI ES QUE SE SELECCIONO
        self.saveEvaluation.clicked.connect(self.guardar)
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
        self.evaluaciones.setText("EVALUACIONES DEL MES: " + str(cantidadEvas))
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
        #print("\n" + str(respuestas))
        if len(respuestas) == 0:
            modelRespuestas = QStandardItemModel(len(respuestas),1)
            #print(len(respuestas))
            headerRespuestas = ['NOT DATA AVAILABLE | NADA QUE VER POR ACA UWU']
            modelRespuestas.setHorizontalHeaderLabels(headerRespuestas)
            self.listaEvaluaciones.setModel(modelRespuestas)
            self.listaEvaluaciones.resizeColumnsToContents()
        else:
            modelRespuestas = QStandardItemModel(len(respuestas),3)
            headerRespuestas = ['PREGUNTA', 'PONDERACION', 'RESPUESTA']
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
    def procesoEva(self):
        self.procesoEvaluado.setText('')
        usuario= self.userFilter.currentText()
        siniestro= self.siniestroFilter.currentText()
        procesoEvaluado= proceso(self, usuario, siniestro)
        self.procesoEvaluado.setText("PROCESO EVALUADO: " + str(procesoEvaluado))
        self.procesoEvaluado.setWordWrap(True)
    def fechaEvaluacion(self):
        self.evaDateUwU.setText('')
        usuario = self.userFilter.currentText()
        siniestro= self.siniestroFilter.currentText()
        firstDate = fechaEva(self,usuario,siniestro)
        if firstDate != 0:
            fechaEvaluacionCRUD = datetime.strptime(str(firstDate),"%Y-%m-%d")
            fechaEvaluacion = fechaEvaluacionCRUD.strftime("%d/%m/%Y")
            self.evaDateUwU.setText('FECHA DE EVALUACION: '+str(fechaEvaluacion))
        else:
            self.evaDateUwU.setText('0')

    #FUNCION PARA GUARDAR LA RETRO EN EL ARCHIVO DE EXCEL
    def guardar(self):
        #Verificamos si el label de la retro no esta vacia
        if self.retro.text():
            #Aqui seteamos las variables para llenar las celdas despues
            empleado = self.userFilter.currentText()
            cantidadEvaluaciones = numEvaluacionesUser(self,empleado)
            siniestro= self.siniestroFilter.currentText()
            procesoEva = proceso(self, empleado, siniestro)
            analistaEvaluador= auditora(self,empleado,siniestro)
            supervisorA = supervisor(self, empleado,siniestro)
            promUsuario= promedioEvaEspecifica(self, empleado, siniestro)
            fechaEvaluacionCRUD = datetime.strptime(str(fechaEva(self,empleado,siniestro)),"%Y-%m-%d")
            fechaRetro = fechaEvaluacionCRUD.strftime("%d/%m/%Y")
            fechaActual = datetime.now()
            fechaEvaluacion = fechaActual.strftime("%d/%m/%Y")
            # Cargar el archivo de Excel existente
            ruta_plantilla = 'media/docs/BLANCO.xlsx' 
            wb = openpyxl.load_workbook(ruta_plantilla)
            sheet = wb.active
            # Modificar el archivo de Excel
            sheet['B2'] = str(empleado)
            sheet['E2'] = str(analistaEvaluador)
            sheet['B3'] = str(procesoEva)
            sheet['E3'] = str(supervisorA)
            sheet['B4'] = str(cantidadEvaluaciones)
            sheet['E4'] = str(promUsuario)
            sheet['C5'] = str(fechaEvaluacion)
            sheet['F5'] = str(fechaRetro)
            sheet['A7'] = self.retro.text()
            sheet['A7'].alignment = Alignment(wrap_text=True)
            sheet['A21'] = str(empleado)
            sheet['B21'] = str(analistaEvaluador)
            sheet['A26'] = str(supervisorA)
            # Oculta la ventana principal de Tkinter
            Tk().withdraw()

            # Mostrar el diálogo para guardar el archivo modificado
            nombreArchivo= str(empleado) + " - " + str(siniestro)
            file_path = asksaveasfilename(defaultextension=".xlsx", 
                                        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                                        title="Guardar archivo como",
                                        initialfile=nombreArchivo)
            if file_path:
                wb.save(file_path)
                #print(f"Archivo guardado como: {file_path}")
                QMessageBox.information(self, "GUARDAR RETRO", "ARCHIVO GUARDADO")
            else:
                #print("No se guardó el archivo.")
                QMessageBox.warning(self, "GUARDAR RETRO", "NO SE GUARDO EL ARCHIVO")
        else:
            QMessageBox.information(self, "GUARDAR RETRO", "SELECCIONE UNA EVALUACION")

    #Funcion para salir
    def salir(self):
        self.close()


#Lo de ley, es como el "Arrancar"
if __name__ == '__main__':
    app = QApplication([])
    dashUsuario= dashUser()
    dashUsuario.show()
    app.exec_()