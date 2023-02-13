## Charts :chart_with_upwards_trend:

Dentro de la carpeta `Charts` nos encontramos con una colección de archivos que describen un conjunto relacionado con recursos de Kubernetes y que harán que se levante nuestra aplicación.
### Contenido de la carpeta Charts

- [app](app) ➢ Aquí nos encontraremos archivos yaml para levantar la aplicación.
- [db](db) ➢ Aquí nos encontraremos también archivos yaml, pero para levantar la base de datos que vamos a utilizar para poder levantar la aplicación.

Dentro de cada una de estas carpetas, nos encontraremos con las siguientes:

- Chart.yaml] ➢ Fichero YAML que contiene información sobre el chart.
- values.yaml ➢ Valores de configuración por defecto del chart.
- templates ➢ Directorio de plantillas que combinado con el fichero values.yaml generan ficheros válidos de manifiesto de Kubernetes. Aquí encontraremos los archivos yaml que describimos anteriormente en el apartado de `K8s`.


Lo primero será levantar minikube:

  ```
  minikube start
  ```

  También deberemos habilitar el `Ingress Controller` en minikube para dar habilitar el controlador de entrada a través del siguiente comando: 
  ```
  minikube addons enable ingress
  ```

- Crearemos un `namespace` (Es un contenedor abstracto en el que un grupo de uno o más identificadores únicos pueden existir) para meter todos los recursos dentro de él:
```
kubectl create namespace app-helm
```
- En el caso de que queramos borrar el namespace:
```
kubectl delete namespace app-helm
```

### Lanzando la base de datos

A fin de levantar la parte de la base de datos deberemos ejecutar el siguiente comando:

- Para poder crear los recursos dentro del namespace:
```
helm -n app-helm upgrade --install db db/
```
 Con este comando ya deberíamos de tener levantada la parte de la base de datos.


 ### Lanzando la aplicación

A fin de levantar la parte de la aplicación deberemos ejecutar el siguiente comando:

- Para poder crear los recursos dentro del namespace:
```
helm -n app-helm upgrade --install app app/
```

Deberemos de esperar unos segundos para que se levante todo correctamente.

Por último, podríamos comprobar que la aplicación está levantada a través de la url que nos ha tenido que aparecer por pantalla cuando hemos ejecutado el comando anterior: http://crisapphelm.192.168.49.2.nip.io/

Al igual que en el apartado de `Docker` y `K8s`, para poder comprobar que nuestra aplicación funciona correctamente, deberemos de ejecutar los siguientes comandos en nuestro navegador:

  - Ver si la aplicación está OK: 
  ```
  http://crisapphelm.192.168.49.2.nip.io/
  ```
  - Para inicializar el contador:
  ```
   http://crisapphelm.192.168.49.2.nip.io/inicializa-contador
   ```
  - Para incrementar el contador:
  ```
   http://crisapphelm.192.168.49.2.nip.io/incrementar-contador
   ```
  - Para ver el valor actual: 
  ```
  http://crisapphelm.192.168.49.2.nip.io/actual
  ```
