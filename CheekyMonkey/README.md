# Implementación de CheekyMonkey 
##### Lisseth Abigail Martinez Castillo
## Introducción
Cheeky Monkey es una herramienta de ingeniería del caos para Kubernetes. Su función es matar aleatoriamente pods en un clúster de Kubernetes para probar su resistencia. En Cheeky Monkey, controlas a un mono que se mueve por tu clúster de Kubernetes. Cuantos más pods tengas, más cajas se lanzan en el juego. Puedes usar las teclas de flecha para mover al mono y la barra espaciadora para golpear las cajas. Cada vez que el mono destruye una caja, se selecciona y elimina aleatoriamente un pod en tu clúster.

    * Puede ayudarte a identificar posibles debilidades en tu clúster de Kubernetes.
    * Puede ayudarte a probar la capacidad de tu clúster para recuperarse de fallos.
    * Puede ayudarte a mejorar la comprensión de tu equipo sobre la ingeniería del caos.
 
 ## Desarrollo
 
 1. Hacer despliegue de un clúster de Kubernetes, para este ejemplo usaremos el mismo de [este ejemplo](https://github.com/lissethamc/practicas-tolerante-fallos/tree/main/kubernetes)
 2. Clonar [este repositorio](https://github.com/richstokes/cheekymonkey) en la computadora local donde se administrará el clúster
 3. Opcional: es posible editar los valores del juego, en el archivo llamado `constance.py`
 4. Ejecutar dentro de la carpeta donde se clonó el repositorio el siguiente comando 
 ```shell
 pip install -r requirements.txt
 ```
 Nota: A día de realización de este documento, se han encontrado inconsistencias con las librerias que se piden instalar.
por lo cual se recomienda quitar el numero de las versiones del archivo `requirements.txt` para que puedan ser instaladas
![image](https://github.com/lissethamc/practicas-tolerante-fallos/assets/33168405/009ed068-7025-4d7e-9aa4-9d2e25bfdcb4)

5. En el archivo `cheekymonkey.py`, en la línea 125 encontramos

```python
self.player = Player("./images/Char_Monkey_Free_Images/Animations/monkey_idle.png", x, y, scale=0.5, moment = _pymunk.inf, mass=1)
```

Es necesario sustituirla por

```python
self.player = Player("./images/Char_Monkey_Free_Images/Animations/monkey_idle.png", x, y, scale=0.5, moment = float("inf"), mass=1)
```
Porque en la libreria pymunk fue removido `_pymunk.inf`

6. Para asegurarnos de que esté funcionando en la consola enlistamos los pods activos con `kubectl get pods`, hay que revisar el campo **age** para ver cuanto tiempo llevan activos los pods antes de ejecutar cheekymonkey

8. Podemos excluir pods que no queremos que sean destruidos al poner sus namespaces en la bandera de exclude
![image](https://github.com/lissethamc/practicas-tolerante-fallos/assets/33168405/a7ce540b-08d2-4960-8cfa-ffae4252fd02)
 
```shell
python cheekymonkey.py --exclude kube-system kube-public kube-node-lease istio-system
```
Con este comando excluimos kube-system, kube-public, kube-node-lease, istio-system

Con esto ya se ejecuta nuestra ventana del cheekymonkey, aunque hubo un error y solo permite eliminar un pod y después de esto crashea el juego
![image](https://github.com/lissethamc/practicas-tolerante-fallos/assets/33168405/4b833a90-92f3-4c3a-a626-94da31f24dd4)

Para demostrar su funcionamiento primero enlistamos los pods que tenemos en DigitalOcean antes de la ejecución

![image](https://github.com/lissethamc/practicas-tolerante-fallos/assets/33168405/35a11785-5a7a-4009-bf14-22be17499608)

Y esto es lo que aparece una vez se destruye un pod
![image](https://github.com/lissethamc/practicas-tolerante-fallos/assets/33168405/afea8473-b709-4224-963f-01123f7b081e)

Este es el listado de pods después de ejecutar cheekymonkey, podemos analizar que el pod de 40m se mantuvo, el de 12s pasó a ser de 104s y el de 51m terminó su ejecución y se levantó uno nuevo teniendo ahora 35s y el menor tiempo
![image](https://github.com/lissethamc/practicas-tolerante-fallos/assets/33168405/f67c432f-79f9-49e2-9bbf-d8c4af8d3866)






