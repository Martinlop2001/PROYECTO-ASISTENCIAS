



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ventana_ui import Ui_MainWindow 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

       
        self.ui.boton_saludo.clicked.connect(s  elf.saludar)

    def saludar(self):
        self.ui.label_resultado.setText("¡Hola desde PyQt5!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())
