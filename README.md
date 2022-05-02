# Guane Intern FastApi

## Interpretación del problema

El software se hizo entendiendo los requisitos que se pedían. Un sistema que simula un sistema de adopción de mascotas donde se puede agregar perros y usuarios. Las funcionalidades son las siguientes:

  - Consultar información de todos los perros registrados
  - Obtener toda la información de un perro mediante su nombre
  - Consultar información de todos los perros adoptados
  - Un usuario puede registrar un nuevo perro
  - Eliminar Perros
  - Actualizar Perros
  - Eliminar usuarios
  - Crear nuevos usuarios
  - Actualizar datos del usuario 
  - Consultar informacion


**Nota:** La operación del POST para los perros esta protegida por una politica de seguridad basada en JWT donde se verifica si el usuario puede acceder a crear perros, se verificará con un token que le fue asignado en el momento de la creación y el correo. 

## Tecnologías

  Este proyecto fue desarrollado usando multiples tecnologías:
  
    - Python 3.8
    - Docker
    - Docker Compose
    - Redis
    - PostgreSQL
    - Celery
    
 ## Uso
 
 Primero, clonar el repositorio para obtener todos los archivos:
 
     - $ git clone https://github.com/Andreaortizg/gttb-042022.git
     
Estando en el directoriio, se configura el ambiente virtual:

    - venv/Scripts/activate
    
Ahora se instala Docker y Docker Compose

Se corren las imágenes

    - docker-compose up 

La aplicación corre por defecto en el puerto 8000, flower en el puerto 5556. 

## Entity Relationship Diagram 

  <img src="/diagrams/DiagramaER.png" alt="Entity Relationship Diagram"/>
  
## Environments

    DATABASE_URL=postgresql+psycopg2://admin:guanedog123@db:5432/admin
    DB_USER=admin
    DB_PASSWORD=guanedog123
    DB_NAME=admin
    PGADMIN_EMAIL=admin@admin.com
    PGADMIN_PASSWORD=admin
    secret_key= "5e3ab9973bfeee8147bd5eb0d6ab37e26d8068b78842c813a79607b47ca9bc6a"
    algorithm = "HS256"
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0 
