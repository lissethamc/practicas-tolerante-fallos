# Monitoreo de clúster de Kubernetes usando Istio y Kiali

#### Lisseth Abigail Martínez Castillo

# ¿Qué es Istio?
Istio es una plataforma de servicio de malla (service mesh) de código abierto que se utiliza para gestionar el tráfico de red en aplicaciones distribuidas y microservicios. Es una herramienta de infraestructura que ayuda a resolver los desafíos comunes que enfrentan las aplicaciones distribuidas, como la resiliencia, la seguridad, la observabilidad y el control del tráfico.

Istio funciona como una capa intermedia entre los servicios de una aplicación, y proporciona funciones de red avanzadas, como balanceo de carga, seguridad de la comunicación entre servicios, enrutamiento de tráfico, control de acceso y monitoreo. También permite la integración con herramientas de terceros para la gestión del tráfico y el análisis de datos.

Istio es compatible con múltiples plataformas y entornos, incluyendo Kubernetes y otros orquestadores de contenedores, entornos de nube pública y privada, y sistemas en bare-metal. Al ser una plataforma de código abierto, la comunidad de desarrolladores puede contribuir al desarrollo y mejora de Istio, lo que permite a los usuarios obtener beneficios adicionales y personalizaciones para sus necesidades específicas.

# Implementación

1. Crear clúster de Kubernetes siguiendo [estos pasos](https://github.com/lissethamc/practicas-tolerante-fallos/tree/main/kubernetes). Es importante hacer un deploy de antemano porque de otra forma Kiali no reconoce qué aplicaciones monitorear.
2. Instalar [Istio](https://github.com/istio/istio/releases/tag/1.17.2), Istio e istioctl, de acuerdo con el sistema operativo.
3. Una vez reconocido el comando `istioctl` creamos el perfil con el comando
```shell
$ istioctl install --set profile=demo -y
```
4. Ejecutamos el comando
```shell
$ kubectl -n istio-system get pods
```
Este comando nos enlista las dependencias necesarias para monitoreo, como: grafana, prometeus, kiali. En este caso las instalaré individualmente.

### Kiali
1.1. Descargar [helm](https://github.com/helm/helm/releases)
1.2. Ejecutar
```shell
helm repo add kiali https://kiali.org/helm-charts
helm repo update
helm install kiali kiali/kiali-server --namespace istio-system
```

### Grafana y Prometeus
1.1. Ejecutar
```shell
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.11/samples/addons/grafana.yaml
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.11/samples/addons/prometheus.yaml
```

Podemos ejecutar de nuevo el comando
```shell
$ kubectl -n istio-system get pods
```
Y de tener las dependencias listas la salida será algo así:
![image](https://user-images.githubusercontent.com/33168405/236783571-d7710418-8a29-4141-a20a-1bdc9b8307e5.png)

5. Antes de iniciar kiali debemos etiquetar el namespace llamado default para que istio pueda monitorearlo, ejecutamos
```shell
$ kubectl label namespace default istio-injection=enabled
```
6. Podemos acceder a la interfaz web de kiali con el siguiente comando
```shell
$ istioctl dashboard kiali
```
Es posible que socilite un token, lo generamos con uno de los siguientes comandos:
```shell
kubectl exec $(kubectl get pod -n istio-system -l app=kiali -o jsonpath='{.items[0].metadata.name}') -n istio-system -- cat /var/run/secrets/kubernetes.io/serviceaccount/token
```
o si diera problemas en windows, podemos usar
```shell
kubectl exec $(kubectl get pod -n istio-system -l app=kiali -o jsonpath='{.items[0].metadata.name}') -n istio-system -- cat /var/run/secrets/kubernetes.io/serviceaccount/token | Out-String | clip.exe
```
Este segundo comando lo guarda automáticamente en el portapapeles.

Una vez dentro, esta es la interfaz
![image](https://user-images.githubusercontent.com/33168405/236784907-182c6a45-9006-4e1c-bc7a-74c3e5f08df7.png)

Seleccionamos Graph en la columna de la izquierda, 

