# Implementación de Docker con ROS

#### 218292645 | Lisseth Abigail Martínez Castillo  :octocat:

### ¿Qué es Docker?
Es una plataforma que permite el despliegue de de aplicaciones en un entorno aislado, en forma de _contenedores_. Los contenedores son instancias que maneja Docker para donde se ejecuta una versión ligera de un sistema operativo. Algunas de las ventajas de usar Docker son:
* __Portabilidad__: Los contenedores de Docker son portátiles, es decir, se pueden ejecutar en cualquier plataforma que tenga Docker instalado, es posible desarrollar una aplicación en una máquina de manera local, pero ejecutarla en cualquier otro entorno, sin preocuparse por la compatibilidad de las plataformas.
* __Consistencia__: Es posible crear entornos de desarrollo y producción idénticos, por lo que las aplicaciones se comportarán de la misma forma en las etapas del ciclo de vida de la aplicación.
* __Aislamiento__: Los contenedores de Docker están aislados entre sí y del sistema operativo host, esto evita conflictos de software y que se afecten entre ellos.
* __Escalabilidad__: Permite agregar o eliminar contenedores según sea necesario para escalar aplicaciones fácilmente.

### ¿Qué es ROS?
Es una plataforma de código abierto que contiene un conjunto de herramientas para facilitar el desarrollo de software y control para robots. Proporciona herramientas para la programación y manejo de robots, así como facilita la estructura para la comuicación entre procesos y control de hardware.

Es también a menudo llamado "metasistema operativo" porque se construye sobre un sisetma operativo subyacente (como Linux), pero proporciona además una capa de abstracción de hardware, herramientas y servicios que permiten comunicación entre los componentes de un robot o sistema robótico (en vez de un sistema operativo tradicional que lo hace a nivel de sistema de computación general). Igualmente proporciona servicios como la gestión y comunicación entre procesos, administración de recursos, entre otras funciones de sistema operativo.
Entre las herramientas que proporciona ROS son las de visualización, simulación, planificación y control de movimiento, percepción y procesamiento de imágenes entre muchas otros.

De las herramientas que proporciona ROS para el manejo de recursos en los sistemas robóticos, es posible considerar sensores, actuadores, planificación de movimiento, entre otros; por lo que en vez de desarrollar software personalizado para cada de estos componentes, es posible usar los servicios de ROS para integrarlos y construir sistemas más complejos. Es decir, nos proporciona una capa de abstracción que permite centrarnos en el desarrollo específico del robot o sistema en vez de preocuparnos por los detalles de bajo nivel o sistema operativo subyacente.

### Implementación

Primero debemos comprobar si tenemos instalado Docker, para ello ejecutamos el siguiente comando en una terminal

```shell
docker --version
```
De tener Docker instalado, debemos ver una salida que indica la versión de docker instalado, sino el comando dará un mensaje de error que indica que el comando "docker" no se encuentra en el sistema.
