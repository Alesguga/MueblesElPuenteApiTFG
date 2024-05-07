# Manual de Despliegue de FastAPI ⚡ en Azure sin Docker

Este manual proporciona una guía paso a paso para subir una aplicación FastAPI desde un repositorio de Git hasta su despliegue en Azure App Service.

## Preparación del Entorno de Desarrollo

### 0. Tener el proyecto de FastAPI listo
    
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### 1. Preparar tu aplicación FastAPI

Asegúrate de que tu aplicación FastAPI esté lista para ser desplegada. Debería tener una estructura de proyecto estándar de FastAPI, incluyendo un archivo `Main.py` (o similar) que contiene la instancia y las rutas de FastAPI.

### 2. Crear un `requirements.txt`

Este archivo contiene todas las dependencias necesarias para tu proyecto. Puedes crearlo ejecutando:

```bash
pip freeze > requirements.txt
```
## Subida de la Aplicación a un Repositorio de Git
```bash
git init
git add .
git commit -m "Initial commit"
```
### 1. Crear un repositorio en GitHub
Damos al boton de new repository le damos un nombre y el tipo de privacidad y ya creamos el repositorio
### 2. Subir tu aplicación a GitHub
```bash
git remote add origin <URL_DEL_REPOSITORIO_REMOTO>
git push -u origin master
```
## Despliegue en Azure App Service sin Docker

### 1. Iniciar sesión en Azure
Busca App Services y crea un nuevo App Service 
### 2. Configurar el App Service
- Grupo de recursos: Crea uno nuevo o selecciona uno existente.
- Nombre de la instancia: Nombre único para tu App Service.
- Plan de ejecución: Selecciona un plan según tus necesidades.
- Región: Elige la más cercana a tus usuarios.
- Pila de ejecución: Elige Python y la versión que corresponde a tu entorno.
- Versión de Python: Selecciona la versión de Python que corresponde a tu proyecto.
### 3. Configurar despliegue desde GitHub
En la configuración del App Service, selecciona "Centro de Despliegue", configura GitHub como la fuente y sigue los pasos para conectar tu repositorio.
### 4. Configurar el comando de Inicio de la Aplicación
En "Configuración" > "Configuración general" de tu App Service, establece el comando de inicio:
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker Main:app
```
### 5. Desplegar la Aplicación
Tras unos minutos unos 6-7 la aplicación debería estar desplegada y accesible en la URL proporcionada por Azure.