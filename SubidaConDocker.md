
# Como subir una api FastAPI⚡en Python 🐍 desde convetirla en Docker 🐋 hasta desplegarla en Azure

<span style="font-family: Segoe UI;">

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Creación de una API con FastAPI](#creación-de-una-api-con-fastapi)
- [Convertirlo a Docker](#convertirlo-a-docker)
- [Despliegue en Azure](#despliegue-en-azure)

## Requisitos

- PyCharm o VsCode con FastApi y Uvicorn
- Docker desktop
- Cuenta con Azure, AWS, Heroku... Cualquier servicio cloud.
- Azure CLI

## Como hacer una Api con FastAPI ⚡

### Instalación de dependencias/librerías
```bash
pip install fastapi
```
```bash
pip install "uvicorn[standard]"
```


En mi caso necesitaba usar muchas fotos para poder ponerlas en la aplicación móvil y en la web por lo cual hice la api en torno a ello pero se puede hacer una muy rapido y fácil con esta docu: https://fastapi.tiangolo.com/tutorial/first-steps/

### Api de prueba

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
Al ejecutar un run te va a salir el puerto donde se ha abierto con el hola mundo en funcionamiento
Saldría algo así:

    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
## Convertirlo a Docker 
<svg  viewBox="0 0 24 24" width="30" height="30" fill="#008fe2">
  <path d="M13.98 11.08h2.12a.19.19 0 0 0 .19-.19V9.01a.19.19 0 0 0-.19-.19h-2.12a.18.18 0 0 0-.18.18v1.9c0 .1.08.18.18.18m-2.95-5.43h2.12a.19.19 0 0 0 .18-.19V3.57a.19.19 0 0 0-.18-.18h-2.12a.18.18 0 0 0-.19.18v1.9c0 .1.09.18.19.18m0 2.71h2.12a.19.19 0 0 0 .18-.18V6.29a.19.19 0 0 0-.18-.18h-2.12a.18.18 0 0 0-.19.18v1.89c0 .1.09.18.19.18m-2.93 0h2.12a.19.19 0 0 0 .18-.18V6.29a.18.18 0 0 0-.18-.18H8.1a.18.18 0 0 0-.18.18v1.89c0 .1.08.18.18.18m-2.96 0h2.11a.19.19 0 0 0 .19-.18V6.29a.18.18 0 0 0-.19-.18H5.14a.19.19 0 0 0-.19.18v1.89c0 .1.08.18.19.18m5.89 2.72h2.12a.19.19 0 0 0 .18-.19V9.01a.19.19 0 0 0-.18-.19h-2.12a.18.18 0 0 0-.19.18v1.9c0 .1.09.18.19.18m-2.93 0h2.12a.18.18 0 0 0 .18-.19V9.01a.18.18 0 0 0-.18-.19H8.1a.18.18 0 0 0-.18.18v1.9c0 .1.08.18.18.18m-2.96 0h2.11a.18.18 0 0 0 .19-.19V9.01a.18.18 0 0 0-.18-.19H5.14a.19.19 0 0 0-.19.19v1.88c0 .1.08.19.19.19m-2.92 0h2.12a.18.18 0 0 0 .18-.19V9.01a.18.18 0 0 0-.18-.19H2.22a.18.18 0 0 0-.19.18v1.9c0 .1.08.18.19.18m21.54-1.19c-.06-.05-.67-.51-1.95-.51-.34 0-.68.03-1.01.09a3.77 3.77 0 0 0-1.72-2.57l-.34-.2-.23.33a4.6 4.6 0 0 0-.6 1.43c-.24.97-.1 1.88.4 2.66a4.7 4.7 0 0 1-1.75.42H.76a.75.75 0 0 0-.76.75 11.38 11.38 0 0 0 .7 4.06 6.03 6.03 0 0 0 2.4 3.12c1.18.73 3.1 1.14 5.28 1.14.98 0 1.96-.08 2.93-.26a12.25 12.25 0 0 0 3.82-1.4 10.5 10.5 0 0 0 2.61-2.13c1.25-1.42 2-3 2.55-4.4h.23c1.37 0 2.21-.55 2.68-1 .3-.3.55-.66.7-1.06l.1-.28Z"/>
</svg> 

Creamos un **requirements.txt** con las librerias que hemos usado
```text
fastapi
uvicorn[standard]
```


Dentro de nuestro IDE creamos un **dockerfile** con las siguientes líneas
```dockerfile
FROM python:3.8
# Establece el directorio de trabajo dentro de tu contenedor de Docker en /app.
WORKDIR /app
#Copia el archivo requirements.txt desde tu directorio local al directorio de trabajo (/app) en el docker.
COPY requirements.txt .
# Instala las dependencias en el docker del requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#Copia el directorio al docker 
COPY . .
#Se informa al docker que el puerto de escucha será el 80
EXPOSE 80
# Se especifica eñ comando que se usa al encender el docker
CMD ["uvicorn", "Subida:app", "--host", "0.0.0.0", "--port", "80"]

```
### A partir de ahora has de haber instalado o tener instalado tanto Docker desktop 🐋 como Azure Cli.

#### El enlace a ambas aplicaciones las dejo aquí mismo:

- https://www.docker.com/products/docker-desktop/
- `La de azure esta un poco mas escondida pero bajas un poco hacia abajo y se ve donde la versión mas reciente`
- https://learn.microsoft.com/es-es/cli/azure/install-azure-cli-windows?tabs=azure-cli

### Desde el CMD la consola de VSCode o desde la consola de PyCharm ejecutar los siguientes comandos

- **Navega hasta tu docker file en cualquier caso** 
```
cd C:\Users\Alejandro\PycharmProjects\ApiMEP\
```
### Construir la imagen del Docker
- Reemplpaza el mi-api por el nombre que le quieras poner, si pones un . al final busca el archivo docker dentro del proyecto

```
docker build -t mi-api .
```
### Verificar si la imagen está construida
    docker images
Se deberia ver mi-api o el nombre que le hayas puesto

### Ejecutar la Imagen del docker 
    docker run -p 80:80 mi-api
    # En caso de ser el 8000
    docker run -p 8000:8000 mi-api
Esto iniciara un contenedor basado en tu imagen y mapeara el puerto 80 del contenedor al puerto 80 del ordenador

Puedes ver si el docker funciona buscando:
    ``http://localhost`` o si tuvieses otro puerto como el 8080 ``http://localhost:8080``

En mi programa por ejemplo cuando lo ejecuto con python lo tengo en el 8000 pero en docker lo tengo para que sea 
directamente con localhost.

## Despliegue en azure

### Recordatorio: tener una cuenta en azure y tener instalado azure CLI
    
1. **Inicia sesión en Azure** _(Recuerda tener el navegador con la cuenta de azure)_
    ```bash
   az login
   ```
2. **Crea un nuevo grupo de recursos**:
    ```bash
        az group create --name miGrupoDeRecursos --location westeurope
    ```
3. **Crea un registro de Contenedores de Azure (ACR)**:
    ```bash
   az acr create --resource-group miGrupoDeRecursos --name miApi --sku Basic
   ```
### Recuerda cambiar los nombres de los grupos de recursos y de los contenedores a los tuyos de preferencia

4. **Inicia sesión en tu registro y actualizalo**
    ```bash
   az acr update --name miApi --sku Standard
   az acr login --name miApi
    ```
5. **Se sube la imagen Docker al registro**
    ```bash
   #Antes de hacer push se ha de etiquetar la imagen
   docker tag prueba9 miApi.azurecr.io/mi-api
   #Nos logeamos en azure cr con el user password que nos entregue
   docker login miApi.azurecr.io -u <username> -p <password>
   #Hacemos el push de la imagen
   docker push miApi.azurecr.io/mi-api
    ```
6. **Verificamos la existencia de la imagen en ACR**
    ```bash
   az acr repository list --name miApi --output table
    ```
7. **Tras ello accedemos a azure**
   - Grupos de recursos 
   - Buscas el recurso
   - Accedes al registro de contenedor
   - Si todo esta bien veras un enlace que te lleva a la Api
</span>









