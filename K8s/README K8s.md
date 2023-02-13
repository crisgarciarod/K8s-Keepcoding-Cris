##  K8s :wheel_of_dharma:

  Dentro de la carpeta `K8s` nos encontramos con los archivos que harán que nuestra aplicación funcione en un entorno. 

  En esta carpeta nos encontraremos con otras dos:

  - [app](app) ➢ Aquí nos encontraremos archivos yaml para levantar la aplicación.
  - [db](db) ➢ Aquí nos encontraremos también archivos yaml, pero para levantar la base de datos que vamos a utilizar para poder levantar la aplicación.

  A continuación, describiremos los archivos yaml:

  - configmap.yaml ➢  Es un objeto de la API que permite almacenar la configuración de otros objetos utilizados.
  - dep.yaml ➢ Es un objeto que puede representar una aplicación de tu clúster.
  - ingress.yaml ➢ Se refiere a un tipo de balanceador de carga especializado para la plataforma, así como otros entornos relacionados con contenedores.
  - secret.yaml ➢ Te permiten almacenar y administrar información confidencial.
  - service.yaml ➢ Es una abstracción que define un conjunto lógico de Pods y una política por la cual acceder a ellos.
  - pvc.yaml ➢ Es la solicitud para suministrar almacenamiento persistente con un tipo y una configuración específicos. 

  Para poder ejecutarlo deberemos de seguir los siguientes pasos:

  Lo primero será levantar minikube (Es una herramienta opensource que mediante la creación de una máquina virtual que  permite disponer de un entorno sencillo de Kubernetes con la mayor parte de sus funcionalidades.) a través del siguiente comando:

  ```
  minikube start
  ```

  También deberemos habilitar el `Ingress Controller` en minikube para dar habilitar el controlador de entrada a través del siguiente comando: 
  ```
  minikube addons enable ingress
  ```

- Crearemos un `namespace` (Es un contenedor abstracto en el que un grupo de uno o más identificadores únicos pueden existir) para meter todos los recursos dentro de él:
```
kubectl create namespace app-k8s
```
- En el caso de que queramos borrar el namespace:
```
kubectl delete namespace app-k8s
```

### Lanzando la base de datos

A fin de levantar la parte de la base de datos, deberemos situarnos dentro de la carpeta `/db` y ejecutar todos los archivos yaml.

- Para poder crear o actualizar los recursos dentro del namespace:
```
kubectl -n app-k8s apply -f 'nombre del archivo del recurso'
```
  Ejemplo: 
```
kubectl -n app-k8s apply -f dep.yaml
```
- En el caso de que queramos borrar los recursos dentro del namespace se hará de la siguiente forma:
```
kubectl -n app-k8s apply -f 'nombre del recurso' 'nombre del archivo del recurso'
```
- Ejemplo: 
```
kubectl -n app-k8s apply -f deployment dep.yaml
```
El orden en el que deberemos de levantar los yaml para que todo nos funcione correctamente, será el siguiente:
- pvc.yaml
- secret.yaml
- service.yaml
- deploy.yaml

### Lanzando la aplicación
A fin de levantar la parte de la aplicación deberemos situarnos dentro de la carpeta `/app` y ejecutar todos los archivos yaml.

- Para poder crear o actualizar los recursos dentro del namespace:
```
kubectl -n app-k8s apply -f 'nombre del archivo del recurso'
```
  Ejemplo: 
```
kubectl -n app-k8s apply -f dep.yaml
```
- En el caso de que queramos borrar los recursos dentro del namespace se hará de la siguiente forma:
```
kubectl -n app-k8s apply -f 'nombre del recurso' 'nombre del archivo del recurso'
```
- Ejemplo: 
```
kubectl -n app-k8s apply -f deployment dep.yaml
```
El orden en el que deberemos de levantar los yaml para que todo nos funcione correctamente, será el siguiente:
- configmap.yaml
- secret.yaml
- ingress.yaml
- service.yaml
- deploy.yaml

Con todo esto levantado, deberíamos de tener la aplicación levantada:

Para comprobarlo deberemos copiar y pegar los siguientes links en nuestro navegador:
  - Ver si la aplicación está OK: 
  ```
  http://crisapp.192.168.49.2.nip.io/
  ```
  - Para inicializar el contador:
  ```
   http://crisapp.192.168.49.2.nip.io/inicializa-contador
   ```
  - Para incrementar el contador:
  ```
   http://crisapp.192.168.49.2.nip.io/incrementar-contador
   ```
  - Para ver el valor actual: 
  ```
  http://crisapp.192.168.49.2.nip.io/actual
  ```