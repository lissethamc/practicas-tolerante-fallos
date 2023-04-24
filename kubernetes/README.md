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


