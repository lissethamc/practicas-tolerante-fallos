from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"form.ui", self)
        self.opValue=-1

    def resultado(self, value):
        val=int(value)
        if val==0:
            print("entro")
            self.answer.setText("No Enteros")
        if val==-1:
            self.answer.setText("error")
        else:
            self.answer.setText(str(val))

