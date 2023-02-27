import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from calculadora import *

def operation():
    startThread(widget, 0, widget.opValue)

def setLabel ():
    index=int(buttons.index(widget.sender()))
    widget.op.setText(buttons[index].text())
    widget.opValue=index

def linkButtons(buttons):
    for i in buttons:
        i.clicked.connect(setLabel) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    buttons=[widget.suma,
             widget.resta,
             widget.mult,
             widget.div
             ]#arreglo de botones para las operaciones
    #widget.opValue=-1 #este valor indicará que operacion se realizará cuando sea presionado enter
    linkButtons(buttons)#enlazamos los botones para que preparen los datos que seran enviados
    widget.enter.clicked.connect(operation)
    widget.show()
    widget.thread={}
    sys.exit(app.exec())