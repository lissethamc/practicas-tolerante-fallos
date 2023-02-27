from threadClass import threadClass
from PyQt5 import QtTest
from random import *


def startThread(widget, index, opValue):
    widget.thread[index]=threadClass(parent=None, value=opValue)#asignamos a una posicion del arreglo un objeto de la clase threadClass que seran nuestros hilos y el objeto adquiere en su atributo index su posicion dentro del arreglo a manera de identificacion
    value1=str(widget.input1.text())
    value2=str(widget.input2.text())
    widget.thread[index].setValues(value1, value2, opValue)
    widget.thread[index].start()#señalizamos que nuestro hilo iniciara su proceso
    widget.thread[index].any_signal.connect(widget.resultado)
