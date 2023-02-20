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

###### Imagen 1: Texto en el bloc de notas al inicio
![img1](https://github.com/lissethamc/practicas-tolerante-fallos/blob/main/Checkpointing/notePad/img1.png)

###### Imagen 2: Texto escrito, esperando a que se ejecute el autoguardado
![img2](https://github.com/lissethamc/practicas-tolerante-fallos/blob/main/Checkpointing/notePad/img2.png)

###### Imagen 3: Archivo de texto generado por la función de autoguardado
![img1](https://github.com/lissethamc/practicas-tolerante-fallos/blob/main/Checkpointing/notePad/img3.png)

# Estatus de la aplicación (Servicios/Daemons)

## Introducción

Es importante predefinir conceptos como **aplicación**, **servicios** y **daemons** pues son utilizados durante el desarrollo de esta práctica:

Las **aplicaciones** son productos de software diseñadas para interactuar con usuarios a través de una interfaz de usuario (GUI), diseñadas para su 
uso en dispositivos móviles, computadoras y otro tipo de dispositivos electrónicos. Los **servicios**, en cambio se ejecutan en segundo plano y no necesitan 
de una interfaz gráfica para proporcionar funciones en el sistema operativo. Un **daemon** es un programa que se ejecuta, igualmente en segundo plano, la diferencia radica
en que generalmente se inicia automáticamente cuando se inicia el sistema operativo. 

Las diferencias entre los daemons y servicios es que los servicios manejan tareas esenciales del sistema, por lo que son ejecutados de manera predeterminada por
el propio sistema operativo, los servicios suelen ser iniciados por el usuario o por una aplicación específica.

## Desarrollo

Para mantener *viva* la aplicación debemos ejecutar a través del módulo *os* para simular la ejecución desde consola la llamada al mismo main del programa; primero verificamos si estamos en Windows o Linux, el programa fue desarrollado en Linux por lo que en este caso está validado para Linux:

```python
def is_closed():
    output = ("python3 main.py", "python main.py")[os.system("cd /home > nul 2>nul")] 
    os.system(f"{output}")
```
Además es necesario identificar cuándo la ventana estará por se cerrada, utilizando:
 
    
```python
    app.aboutToQuit.connect(is_closed)
```

Eso mantiene la ventana abierta y llamando a nuestro programa desde la conosola a pesar de que sea cerrada por el usuario, pero aún es necesario ejecutar el servicio desde el sistema operativo, para eso es necesario configurarlo

Creamos nuestro servicio con el siguiente comando en la terminal de Linux `sudo nano <test>.service`, para configurar el archivo de la siguiente forma:

```systemd
    [Unit]
    Description=My test service
    After=multi-user.target
    StartLimitIntervalSec=0
    [Service]
    Environment=DISPLAY=:0
    Environment=XAUTHORITY=/home/<lissethamc>/.Xauthority
    Type=simple
    Restart=on-failure
    RestartSec=1
    User=<lissethamc>

```
Una vez con ese servicio ponemos los siguientes comandos en la consola para utilizar el servicio

