# Proyecto del sistema ALA (Abstracci贸n de Ludificaci贸n Adaptativa)


## Pre-requisitos 馃搵

```
-Python 3.8 (Se recomienda utilizar un entorno virtual)

-Se debe crear un archivo .env con las variables para configurar el entorno.
```
## Instalaci贸n 馃敡
```
-Para la instalaci贸n de todas las dependencias necesarias para el correcto funcionamiento del sistema se debe ejecutar 
el siguiente comando: pip install -r requirements.txt

-Ejecutar los siguientes comandos para realizar las migraciones de las tablas a la base de datos: 
python3 manage.py makemigrations
python3 manage.py migrate

-Ejecutar el siguiente comando para cargar informaci贸n (Usuarios, d铆as, criterios de valoraci贸n) en la base de datos: 
python3 manage.py loaddata data.json

-Configurar el fichero .env (Base de datos a utilizar, dominio, nombres en los botones) que se encuentra dentro del proyecto:

#DB
MYSQL_HOST='valor'
MYSQL_USER='valor'
MYSQL_PASSWORD='valor'
MYSQL_DB='valor'
MYSQL_PORT=''

#SERVICE_EMAIL
EMAIL_BACKEND='valor'
EMAIL_HOST='valor'
EMAIL_USE_TLS='valor'
EMAIL_PORT='valor'
EMAIL_HOST_USER='valor'
EMAIL_HOST_PASSWORD='valor'
  
#DOMAINS
DEFAULT_DOMAIN = 'http://localhost:8000'

#NAVBAR_COLOR
NAVBAR_COLOR = 'bg-info'

#ROOT_NAVBAR
ROOT_CREATE_ADMIN='Alta de admin'
ROOT_CREATE_PROJECT='Crear proyecto'
#

#ROOT_HEADER
ROOT_HEADER='Como Root tiene acceso a crear projectos y asignarselos a los usuarios administradores, desde las opciones en el men煤 de su izquierda'
#

#PROJECT_TITLE
PROJECT_TITLE='ALA'
#

#ADMIN_NAVBAR
ADMIN_CREATE_BADGE='Crear Insignia'
ADMIN_CREATE_CHALLENGE='Crear Desaf铆o'
#

#PLAYER_NAVBAR
PLAYER_CREATE_CHECKIN='Realizar checkin'
PLAYER_SEE_MY_GE='Ver mis EJ'
PLAYER_SEE_ALL_PROJECTS='Todos los proyectos'
PLAYER_MY_PROJECTS='Mis proyectos'
#

#TIME_RESTRICTION
CREATE_TIME_RESTRICTION='Crear RT'
#

#BUTTON
REGISTER_BUTTON='Unirme'
MODIFY_BUTTON='Modificar'
DISJOIN_BUTTON='Dar Baja'
#
```

## Despliegue de la aplicaci贸n 馃摝
```
python3 manage.py runserver
```
## Ejecuci贸n de los tests 馃敡
```
python3 manage.py test
```

## Autores 鉁掞笍

* **Micael Jotar** - *Trabajo Completo* - [jotarMicael](https://github.com/jotarMicael).
* **Valentin Gallardo Ucero** - *Trabajo Completo*.

  
