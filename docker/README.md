# Implementación de HelloWorld Docker con ROS

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

Docker puede ser utilizado con diferentes distribuciones de ROS, algunas de las versiones compatibles con Docker son:
* ROS Kinetic Kame
* ROS Melodic Morenia
* ROS Noetic Ninjemys
* ROS2 Dasing Diademata
* ROS2 ELoquent Elusor
* ROS2 Fosy Fitzroy
Entre otros

Es necesario primero asegurarnos que la imagen de Docker es compatible con la distribución de Linux que estamos usando, aunque las imágenes de Docker para ROS suelen ser para una distribucion de Linux en especifica como Ubuntu.

No todas las distribuciones de ROS son compatibles con Docker pero la mayoría lo son, se recomienda usar una versión de ROS que tenga soporte activo y se actualice regularmente. Si se usa una versión de ROS menos común es probable que no haya una versión de Docker disponible o se deba de construir una imagen personalizada.

Es posible utilizar Docker con prácticamente cualquier distribución de Linux y las imágenes de Docker para ROS suelen estar construidas para Ubuntu. Si se usa una distrubición de Linux diferente, es posible que sea necesario ajustar la configuración de Docker y ROS para asegurarnos del correcto funcionamiento.

**Nota**: No es necesario tener instalado ROS de antemano en el sistema host para poder correrlo en un entorno Docker, ese es el objetivo de instalar Docker

###### Instalación de Docker en Linux

Primero debemos comprobar si tenemos instalado Docker, para ello ejecutamos el siguiente comando en una terminal

```shell
docker --version
```
De tener Docker instalado, debemos ver una salida que indica la versión de docker instalado, sino el comando dará un mensaje de error que indica que el comando "docker" no se encuentra en el sistema.

Para instalar Docker en caso de ser necesario

1. Actualizar los paquetes del sistema:
```shell
sudo apt-get update
```

2. Instalar los paquetes necesarios utilizar paquetes via HTTPS:
```shell
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```

3. Descargar e importar la clave GPG oficial de Docker:
```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
4. Agregar el repositorio de Docker a las fuentes de paquetes de APT:
```shell
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
5. Actualizar de nuevo los paquetes del sistema para que sea posible reconocer los paquetes de Docker recién agregados
```shell
sudo apt-get update
```

6. Instalar Docker
```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Podemos confirmar su instalación ejecutando el comando
```shell
docker run hello-world
```
Esto nos descarga una imagen de prueba y la ejecuta en un contenedor de Docker, mostrando su correcto funcionamiento.

###### Descargar y correr una imagen de ROS en Docker

Para poder trabajar con ROS, necesitamos una imagen de Docker, es decir un sistema operativo que tenga pre instalado ROS. Podemos descargar una imagen desde Docker Hub, Por ejemplo, podemos descargar la última imagen de ROS Melodic, corremos el siguiente comando en una terminal (es probable que estos comandos necesiten permisos de superusuario):

```shell
docker pull ros:melodic
```
