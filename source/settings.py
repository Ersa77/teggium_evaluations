from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtGui import QIcon

class settings(QMainWindow):    
    def __init__(self):
        super().__init__()
        loadUi('interfaces/analista_calidad/systemSettings.ui', self)
        self.setWindowIcon(QIcon('media/icons/icon_app.ico'))
        self.setWindowTitle('GESTION DE USUARIOS')
        self.close_config.clicked.connect(self.closeSettings)

    def closeSettings(self):
        self.close()
    
if __name__ == "__main__":
    app = QApplication([])
    settingsWindow = settings()
    settingsWindow.show()
    app.exec_()
