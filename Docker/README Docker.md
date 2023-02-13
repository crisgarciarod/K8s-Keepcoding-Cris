##  Docker :computer:

Dentro de la carpeta `Docker` nos encontramos con los archivos que harán que nuestra aplicación funcione en local.

### Contenido de la carpeta Docker

Dentro de la carpeta Docker, nos encontraremos con el siguiente contenido: 

- [.env](.env) ➢ Aquí nos encontraremos todas las variables de entorno que hemos utilizado.
- [app.py](app.py) ➢ Aquí estará nuestra aplicación flask escrito en python.
- [db.sh](db.sh) ➢ Aquí nos encontramos nuestra base de datos en script.
- [docker-compose.yaml](docker-compose.yaml) ➢ Aquí construye la imagen del contenedor y lanza todo el entorno en local.
- [Dockerfile](Dockerfile) ➢ Aquí se incluye una serie de instrucciones que se necesitan ejecutar de manera consecutiva para cumplir con los procesos necesarios para la creación de una nueva imagen.
s
### Lanzando la aplicación

Para construir la imagen del contenedor y probar la aplicación deberemos de ejecutar los siguientes comandos:

- Para crear la imagen:

```
docker-compose build -t crisgarcia/python:3.7-alpine
```
- Para probar la aplicación:
```
docker-compose up -d
```

Para comprobar el acceso tendremos que copiar los siguientes links en nuestro navegador:
  - Ver si la aplicación está OK: 
  ```
  http://localhost:5000
  ```
  - Para inicializar el contador:
  ```
   http://localhost:5000/inicializa-contador
   ```
  - Para incrementar el contador:
  ```
   http://localhost:5000/incrementar-contador
   ```
  - Para ver el valor actual: 
  ```
  http://localhost:5000/actual
  ```

  Ejecutando lo anteriormente dicho, no deberíamos de tener problemas de levantar nuestra aplicación en local.