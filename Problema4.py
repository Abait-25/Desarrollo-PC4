"""
Tienes un fichero temperaturas.txt que contiene registros de temperaturas diarias en formato
CSV. Cada línea del fichero tiene la siguiente estructura: fecha,temperatura. Debes leer el
fichero, calcular la temperatura promedio, la temperatura máxima y la mínima. Finalmente,
debes escribir los resultados en un nuevo fichero resumen_temperaturas.txt.
"""

import requests
url = 'https://github.com/gdelgador/ProgramacionPython202407/raw/main/Modulo4/src/temperaturas.txt'
archivo_temperaturas = 'temperaturas.txt'
archivo_resumen = 'resumen_temperaturas.txt'

try:
    respuesta = requests.get(url)
    respuesta.raise_for_status()  # Lanza una excepción para códigos de estado 4xx/5xx
    with open(archivo_temperaturas, 'wb') as archivo:
        archivo.write(respuesta.content)
    print(f'Archivo de temperaturas descargado y guardado como {archivo_temperaturas}')
except requests.RequestException as e:
    print(f'Error al descargar el archivo: {e}')
    exit(1)

temperaturas = []
try:
    with open(archivo_temperaturas, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) == 2:
                try:
                    temperatura = float(partes[1])
                    temperaturas.append(temperatura)
                except ValueError:
                    print(f'Valor de temperatura no válido en la línea: {linea}')
except FileNotFoundError:
    print(f'El archivo {archivo_temperaturas} no se encuentra.')
    exit(1)

if temperaturas:
    promedio = sum(temperaturas) / len(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)
    
    try:
        with open(archivo_resumen, 'w') as archivo:
            archivo.write(f'Temperatura Promedio: {promedio:.2f}\n')
            archivo.write(f'Temperatura Máxima: {maxima:.2f}\n')
            archivo.write(f'Temperatura Mínima: {minima:.2f}\n')
        print(f'Resumen de temperaturas guardado en {archivo_resumen}')
    except IOError as e:
        print(f'Error al escribir el archivo de resumen: {e}')
else:
    print('No se encontraron temperaturas válidas en el archivo.')
