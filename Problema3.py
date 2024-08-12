"""
Descargue la imagen que más le agrade, según lo revisado en la clase. Posteriormente crear un
programa que permita el almacenamiento de la imagen como un archivo zip. Finalmente cree
un código que permita hacer un unzip al archivo zipeado.

"""

import requests
import zipfile
import os

# URL de la imagen
url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

# Nombre del archivo de la imagen y del archivo ZIP
nombre_imagen = 'imagen_descargada.jpg'
nombre_zip = 'imagen.zip'

# Paso 1: Descargar la imagen
try:
    respuesta = requests.get(url)
    respuesta.raise_for_status()  # Lanza una excepción para códigos de estado 4xx/5xx
    with open(nombre_imagen, 'wb') as archivo:
        archivo.write(respuesta.content)
    print(f'Imagen descargada y guardada como {nombre_imagen}')
except requests.RequestException as e:
    print(f'Error al descargar la imagen: {e}')

# Paso 2: Crear el archivo ZIP con la imagen
try:
    with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
        archivo_zip.write(nombre_imagen, os.path.basename(nombre_imagen))
    print(f'Archivo ZIP creado: {nombre_zip}')
except Exception as e:
    print(f'Error al crear el archivo ZIP: {e}')

# Paso 3: Descomprimir el archivo ZIP
carpeta_destino = 'descomprimido'
os.makedirs(carpeta_destino, exist_ok=True)  # Crear la carpeta si no existe

try:
    with zipfile.ZipFile(nombre_zip, 'r') as archivo_zip:
        archivo_zip.extractall(carpeta_destino)
    print(f'Archivo ZIP descomprimido en la carpeta: {carpeta_destino}')
except Exception as e:
    print(f'Error al descomprimir el archivo ZIP: {e}')