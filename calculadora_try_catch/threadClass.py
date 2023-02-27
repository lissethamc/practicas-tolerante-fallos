from PyQt5 import QtCore
from PyQt5 import QtTest
from random import *
from mainwindow import *
from main import *
import string

class threadClass(QtCore.QThread):#la clase threadClass generará un objeto que contenga un hilo pero que ademas podamos modificar su comportamiento mediante metodos de la misma clase que serán reeimplementados
    any_signal=QtCore.pyqtSignal(int)#any_signal sera una señal que activirá los slots en los cuales se utilice el connect() similar al comportamiento de un boton, una señal dada iniciara un slot que se haya especificado en el codigo
    operation_signal=QtCore.pyqtSignal(int)

    def __init__(self, parent= None, value=0):
        super(threadClass,self).__init__(parent)
        self.value=value
        self.is_running=True#y activamos la bandera de que el hilo está corriendo
        self.terminate=False#seteamos que terminate es falso para que pueda ejecutarse de manera correcta y para despues cambiar su valor a false cuando sea necesario
        self.input1=0
        self.input2=0
        self.opValue=0
        self.error=0

    def run(self):#citando la documentacion de QT "You can reimplement this function to facilitate advanced thread management. Returning from this method will end the execution of the thread."
        print(f"starting thread: operacion: {self.value}")#informacion sobre que "hilo se esta iniciando"
        try:
            resultado=self.operation(self.opValue)
            self.any_signal.emit(resultado)

        except:
            self.any_signal.emit(self.error)#emitimos otra señal para que se acumule en la barra de tareas
            print("error detectado")
            self.stop()
            return
        #self.any_signal.emit(cnt)#emitimos otra señal para que se acumule en la barra de tareas
        self.stop()
                

    def stop(self):
        self.terminate=True
        self.is_running=False

    def setValues(self,value1, value2, opValue):
        self.input1=value1
        self.input2=value2
        self.opValue=opValue
    
    def operation(self,opValue):
        #este bloque if-else es para verificar si son digitos las inputs
        if self.input1.isdigit() and self.input2.isdigit():
            valor1=int(self.input1)
            valor2=int(self.input2)
        else:
            self.error=-1
            print("valores no enteros")
            raise ValueError('valores no enteros')
        if opValue==-1:
            self.error=-1
            print("no operation")
            raise ValueError('no operation')

        if opValue==0:
            resultado=valor1+valor2
        if opValue==1:
            resultado=valor1-valor2
        if opValue==2:
            resultado=valor1*valor2
        if opValue==3:
            resultado=valor1/valor2
        return resultado
    