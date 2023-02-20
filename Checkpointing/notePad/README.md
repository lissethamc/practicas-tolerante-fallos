Lisseth Abigail Martínez Castillo | 218292645
# Checkpointing
## Introducción
Es una técnica en la programación de aplicaciones críticas y de alta disponibilidad, la cual nos permite guardar el estado actual de una aplicación en un momento específico para su posterior recuperación en caso de fallas o interrupciones.
Existen diferentes técnicas para hacer *checkpointing*, por ejemplo:
* Basado en disco: Consiste en escribir el estado actual de una aplicación en un archivo del disco.
* Basado en replicación: Se mantiene una copia del estado actual en un segundo servidor o máquina.
* Basado en memoria: Se realiza una copia del estado de la aplicación en la memoria principal. Es más rápida que las otras dos técnicas.
* Basado en bases de datos: La base de datos se puede recuperar en caso de una falla o interrupción.

## Desarrollo
Para esta práctica se está usando *checkpointing basado en disco*, se implementa un *autosave* en un bloc de notas utilizando el módulo **apscheduler** de Python

```python
def scheduledMethods():
    scheduler = BackgroundScheduler()
    scheduler.add_job(autoSave, 'interval', seconds=30)
    scheduler.start()
```
Este autosave es ejecutado cada 30 segundos, es decir la escritura de lo que se encuentre en el bloc de notas se almacena en un archivo de texto cada 30 segundos

```python
def autoSave():
    widget.statusBar().showMessage("autosaved!")
    QtTest.QTest.qWait(500)
    retrievedText = widget.plainTextEdit.toPlainText()
  

    newFile = open("autosaved.txt","w")
    newFile.write(retrievedText)
    newFile.close()
    widget.statusBar().showMessage("")
```
Función aparte del guardado manual, además de que al iniciar la ejecución del programa, si el archivo de autoguardado no está vació, mostrará lo que se haya guardado automáticamente, asumiendo que se cerró sin haberse guardado correctamente.


# Estatus de la aplicación (Servicios/Daemons)

## Introducción

Es importante predefinir conceptos como **aplicación**, **servicios** y **daemons** pues son utilizados durante el desarrollo de esta práctica:

Las **aplicaciones** son productos de software diseñadas para interactuar con usuarios a través de una interfaz de usuario (GUI), diseñadas para su 
uso en dispositivos móviles, computadoras y otro tipo de dispositivos electrónicos. Los **servicios**, en cambio se ejecutan en segundo plano y no necesitan 
de una interfaz gráfica para proporcionar funciones en el sistema operativo. Un **daemon** es un programa que se ejecuta, igualmente en segundo plano, la diferencia radica
en que generalmente se inicia automáticamente cuando se inicia el sistema operativo. 

Las diferencias entre los daemons y servicios es que los servicios manejan tareas esenciales del sistema, por lo que son ejecutados de manera predeterminada por
el propio sistema operativo, los servicios suelen ser iniciados por el usuario o por una aplicación específica.




