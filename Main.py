from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import requests
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# URL base donde están almacenadas todas las imágenes
base_url = "https://gutigut.com/FotosWeb"

# Asegurar que la base_url termina con '/'
if not base_url.endswith('/'):
    base_url += '/'

@app.get("/")
async def root():
    return {
        "endpoints": {
            "List folders and images": "/folders/{path:path}",
            "Get specific image": "/images/{path:path}/{image_name}",
        }
    }

def parse_directory_index(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        # Asegurarse de que las URLs para carpetas terminan con '/' y son correctas
        folders = [url + (link.get('href') if link.get('href').startswith('/') else '/' + link.get('href')) for link in links if link.get('href').endswith('/') and not link.get('href').startswith('?')]
        images = [url + (link.get('href') if link.get('href').startswith('/') else '/' + link.get('href')) for link in links if not link.get('href').endswith('/') and not link.get('href').startswith('?')]
        return folders, images
    except requests.RequestException:
        raise HTTPException(status_code=404, detail="Unable to retrieve directory listing")

@app.get("/folders/{path:path}")
async def list_folders_and_images(path: str = ""):
    full_url = f"{base_url}{path}" if path else base_url
    folders, images = parse_directory_index(full_url)
    return {"folders": folders, "images": images}

@app.get("/images/{path:path}/{image_name}")
async def get_image(path: str, image_name: str):
    full_image_url = f"{base_url}{path}/{image_name}" if path else f"{base_url}/{image_name}"
    return RedirectResponse(full_image_url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)