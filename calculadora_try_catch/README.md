# Uso de hilos para manejo de errores en tiempo real
El uso de hilos en esta aplicación tiene como funcion el manejar no solo las operaciones que el usuario realice
sino tambien para el manejo de errores dentro de las entradas o en la ausencia de ellas.
en este caso el programa mantiene la aplicacion en ejecucion y lanza mensajes de error en dos casos:
- uno o ambos caracteres no son numeros
- no se seleccionó que operación para realizar con las entradas

justamente el hilo maneja la operacion, valida las entradas y su tipo de dato.
El problema que se presentan con los programas con interfaz grafica es que si un error aparece, esta cierra de manera abrupta sin presentar mas informacion
solo en consola pero en muchos casos el usuario no tiene acceso a la interfaz por lo tanto resulta importante el manejo de errores para dos cosas:
- que la aplicación no cierre
- el usuario conozca que hubo un error y la información de dicho error.

el uso de hilos con QT es bastante peculiar, ya que QT proporciona la posibilidad para añadir codigo a las rutinas como start() o stop()
para poder manipular el comportamiento del hilo.

con esto podemos realizar nuesto procesamiento cuando lanzamos el hilo.

La interfaz es bastante simple:

![image](https://user-images.githubusercontent.com/33168405/221622786-3aec35d3-2b7e-448c-9b16-ae957781faa8.png)

tenemos dos entradas y botones que señalan operaciones para realizar y un boton para ejecutar la operacion:

![image](https://user-images.githubusercontent.com/33168405/221623157-0846d5e1-9f15-4803-8106-035020d272ca.png)

el manejo de errores se da cuando no tenemos operador pero si entradas y cuando uno o ambas entradas no son digitos:
- no hay operador:

  ![image](https://user-images.githubusercontent.com/33168405/221623517-73084f8c-0114-460f-bba0-fc7340c5094c.png)
  
  - la entrada en pantalla solo muestra el error, en consola se muestra:
  
  ![image](https://user-images.githubusercontent.com/33168405/221623843-4eb8a306-4199-4aba-a0b0-133b81f5744d.png)

  
- uno o ambos operadores no son digitos:
  
  ![image](https://user-images.githubusercontent.com/33168405/221624199-cac1e33e-0ab5-45bb-befe-5e5b103b32ce.png)
  
  - en consola se muestra:
  
  ![image](https://user-images.githubusercontent.com/33168405/221624357-870f1d34-beb5-495d-9626-0f4ee1e9aad2.png)


la rutina que maneja los errores es la siguiente (dentro de threadClass.py):
```python
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
```

justamente podemos observar que realiza un bloque try catch con una funcion, está funcion a ala vez maneja otros errores.
es importante que se maneje en esta parte pero tambien adentro para detectar que tipo de error dió, tambien se podria extender el bloque try catch para
manejar distintos errores

la funcion que opera es la siguiente (dentro de threadClass.py):

```python
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
```

podemos aprecia que es bastante basica pero lo que se busca es simplemente detectar errores
esto se hace con una varibale dentro del objeto llamada "error"
esta clase ademas de manejar el hilo, emite señales que manipulan los objetos de la interfaz para mostrar resultados, la señal es enlazada a una función la cual
resivirá datos mediante la señal declarada como any_signal (dentro de threadClass.py):
``` python
 class threadClass(QtCore.QThread):
    any_signal=QtCore.pyqtSignal(int)
    operation_signal=QtCore.pyqtSignal(int)
```
any_signal manda una señal a la ventana para que haga dos cosas (dentro de mainWindow.py):
- mande una señal de error y muestre que hubo un error en pantalla
- ponga el resultado en pantalla
``` python
def resultado(self, value):
        val=int(value)
        if val==0:
            print("entro")
            self.answer.setText("No Enteros")
        if val==-1:
            self.answer.setText("error")
        else:
            self.answer.setText(str(val))
```
donde value es el valor que emite la señal en el metodo run()
