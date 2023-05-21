# Implementación de CheekyMonkey 
##### Lisseth Abigail Martinez Castillo
## Introducción
Cheeky Monkey es una herramienta de ingeniería del caos para Kubernetes. Su función es matar aleatoriamente pods en un clúster de Kubernetes para probar su resistencia. En Cheeky Monkey, controlas a un mono que se mueve por tu clúster de Kubernetes. Cuantos más pods tengas, más cajas se lanzan en el juego. Puedes usar las teclas de flecha para mover al mono y la barra espaciadora para golpear las cajas. Cada vez que el mono destruye una caja, se selecciona y elimina aleatoriamente un pod en tu clúster.

    * Puede ayudarte a identificar posibles debilidades en tu clúster de Kubernetes.
    * Puede ayudarte a probar la capacidad de tu clúster para recuperarse de fallos.
    * Puede ayudarte a mejorar la comprensión de tu equipo sobre la ingeniería del caos.
 
 ## Desarrollo
 
 1. Hacer despliegue de un clúster de Kubernetes, para este ejemplo usaremos el mismo de (este ejemplo)[https://github.com/lissethamc/practicas-tolerante-fallos/tree/main/kubernetes]
 
