# Proyecto de ciencia creativa


### Pre-requisitos 📋

```
-Instalar un entorno virtual para Python 3.8

-Se debe crear un archivo .env con las siguientes variables para configurar el entorno:
```
...
### Instalación 🔧
```
pip install -r requirements.txt

.env:

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

#SET DEFAULT DATA
#python manage.py loaddata data.json

#NAVBAR_COLOR
NAVBAR_COLOR = 'bg-info'

#ROOT_NAVBAR
ROOT_CREATE_ADMIN='Alta de admin'
ROOT_CREATE_PROJECT='Crear proyecto'
#

#ROOT_HEADER
ROOT_HEADER='Como Root tiene acceso a crear projectos y asignarselos a los usuarios administradores, desde las opciones en el menú de su izquierda'
#

#PROJECT_TITLE
PROJECT_TITLE='ALA'

#

#ADMIN_NAVBAR
ADMIN_CREATE_BADGE='Crear Insignia'
ADMIN_CREATE_CHALLENGE='Crear Desafío'
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
```

## Despliegue 📦
```
Python: python3 manage.py runserver
```
## Autores ✒️

* **Micael Jotar** - *Trabajo Completo* - [jotarMicael](https://github.com/jotarMicael)


  
