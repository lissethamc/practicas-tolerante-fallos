# Implementación con Kubernetes
### 218292645 | Lisseth Abigail Martínez Castillo

## ¿Qué es Kubernetes?
Es una plataforma de orquestación de contenedores de código abierto, quiere decir que en vez de tener que administar cada contenedor individualmente, una plataforma como Kubernetes permite a los desarrolladores y administradores de sistemas tratar a los contenedores como una sola unidad lógica. 

Dentro de las tareas que se realizan durante el ciclo de vida de los contenedores están su despliquegue en los servidores, la configuración de la red, asignación de recursos, monitoreo de su estado y actualización de la aplicación. 

Permite además la gestión através de múltiples plataformas diferentes como nubes públicas, privadas o en infraestructura local.

## ¿Qué es Ingress?
Es una funcionalidad de Kubernetes usada para administrar el acceso através de HTTP y HTTPS en el exterior de los clústeres de Kubernetes. Permite el enrutamiento de tráfico a servicios dentro de los clústeres de Kubernetes en función de las reglas configuradas por el usuario. Podría verse como un intermediario entre los servicios del clúster y el mundo exterior.

## ¿Qué es un LoadBalancer?
Es un componente que distribuye el tráfico de red entre múltiples servidores o instancias de aplicación, con el objetivo de mejorar el rendimiento, escalabilidad y disponibilidad de las aplicaciones, de esta forma los servidores tienen una carga de trabajo equilibrada. 

El balanceador puede tomar decisiones sobre qué servidor enviar cada solicitud utilizando algoritmo como round-robin, peso, IP hash, etc.

Pueden ser de hardware o de software, se utilizan en aplicaciones web, empresariales, servicios en la nube, servicios de transmisión de video o entornos de alta demanda.

En Kubernetes, los balanceadores de carga se utilizan para exponer los servicios a través de una dirección IP externa y distribuir el tráfico de los pods que ejecutan los contenedores de la aplicación. Proporciona balanceadores de carga de nube, de servicio, de ingreso que se usan según los requisitos de la aplicación e infraestructura.

## Desarrollo

###### Prerrequisitos
Para poder administrar Kubernetes en DigitalOcean desde consola en este reporte fue necesario instalar [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/), [doctl](https://docs.digitalocean.com/reference/doctl/) y [Docker Engine](https://docs.docker.com/engine/)

###### Kubernetes en DigitalOcean
Para la implementación, una vez creada una cuenta en DigitalOcean, en la página principal nos da la opción de hacer un deploy en un ambiente de contenedores, seleccionaremos esa opción, una vez dentro podemos ajustar los parámetros, por ejemplo es importante seleccionar la locación del datacenter pues juega un papel importante en la rapidez de respuesta de las peticiones
![image](https://user-images.githubusercontent.com/33168405/233978343-b40d361a-531a-454f-a774-40606007cdb9.png)

La selección de parámetros varía las cuotas de uso, por ejemplo el autoescalado indicará si la capacidad de pods seleccionada inicialmente es insuficiente, si se crean nuevos pods. Es importante tener en cuenta el sistema que será necesario pues es probable que se apliquen cargos

![image](https://user-images.githubusercontent.com/33168405/233978797-6d03368f-a74a-4895-b6cd-a73f948b0b87.png)

En la parte de abajo podemos asignar este cluster a algún proyecto existente, lo que quiere decir si en un futuro queremos escalar el proyecto a más clústeres esta es la parte donde deben ser añadidos, al finalizar nos da un total del costo del servicio. Seleccionamos **create cluster**.

![image](https://user-images.githubusercontent.com/33168405/233979396-c84cb06b-215b-4f6e-b703-f4a227042969.png)

Puede tomar un tiempo en configurarse el entorno pero estará listo cuando aparezca una interfaz como la siguiente:
![image](https://user-images.githubusercontent.com/33168405/233980088-50d2f84f-a127-4db2-b43d-927421a03189.png)

Es importante tener a la mano el cluster ID pues se usará para pasos siguientes.
###### Deploy
Ahora es necesario autenticarnos con [doctl](https://docs.digitalocean.com/reference/doctl/)
Es necesario tener los archivos que utilizaremos en una sola carpeta, abrimos una consola de comandos en esa carpeta, en esa consola ejecutamos el comando

```shell
docker build -t my-python-app .
```

Después de eso vamos a crear la imagen del contenedor que se subirá, lo subimos a nuestro proyecto en digital ocean y creamos su deployment cambiando **`<your-registry-name>`** por el nombre de nuestro clúster, en este caso sera python-flask-app

```shell
doctl registry create Python-flask-app
docker tag my-python-app registry.digitalocean.com/<your-registry-name>/my-python-app
docker push registry.digitalocean.com/<your-registry-name>/my-python-app
  
doctl registry kubernetes-manifest | kubectl apply -f -
kubectl create deployment my-python-app --image=registry.digitalocean.com/<your-registry-name>/my-python-app
```

![image](https://user-images.githubusercontent.com/33168405/233983845-31f4eea9-d887-49a9-840d-2b4020e60f55.png)

Una vez hecho esto podemos hacer una réplica con el comando
```shell
kubectl scale deployment/my-python-app --replicas=2
kubectl create deployment my-python-app --image=registry.digitalocean.com/<your-registry-name>/my-python-app
```
Y para añadir el servicio de balanceador de cargas usar el siguiente comando
```shell
kubectl expose deployment my-python-app --type=LoadBalancer --port=80 --target-port=80
```
Y este comando nos permite monitorear el estado del balanceador de cargas
```shell
doctl compute load-balancer list --format Name,Created,IP,Status
```
![image](https://user-images.githubusercontent.com/33168405/233984350-25647672-a511-48fd-93b1-cb767dd7e393.png)

Al ingresar a la IP podemos ver el deploy de nuestra App


![image](https://user-images.githubusercontent.com/33168405/233985024-79885c9a-1b70-4954-88c0-790641fd12b9.png)
