"""
Implemente un programa donde se le solicitará al usuario la ruta de un archivo .py (nombre y
ruta). Y retorne la cantidad de líneas de código de ese archivo, excluyendo los comentarios y
líneas en blanco. Si el usuario ingresa una ruta inválida o si el nombre del archivo no termina en
.py, su programa no retornará ningún resultado.

"""
import os

def contar_lineas_codigo(ruta_archivo):
    """Cuenta las líneas de código en un archivo .py, excluyendo comentarios y líneas en blanco."""
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        # Contar líneas de código, ignorando comentarios y líneas en blanco
        num_lineas_codigo = 0
        for linea in lineas:
            linea = linea.strip()  # Eliminar espacios en blanco al inicio y al final
            if linea and not linea.startswith('#'):  # Línea no vacía y no es un comentario
                num_lineas_codigo += 1
        
        return num_lineas_codigo
    
    except FileNotFoundError:
        print(f'El archivo {ruta_archivo} no se encuentra.')
        return None
    except Exception as e:
        print(f'Error al leer el archivo: {e}')
        return None

def main():
    # Solicitar la ruta del archivo al usuario
    ruta_archivo = input('Introduce la ruta del archivo .py: ').strip()
    
    # Validar que el archivo tiene la extensión .py
    if not ruta_archivo.endswith('.py'):
        print('El archivo no tiene la extensión .py.')
        return
    
    # Contar las líneas de código
    num_lineas_codigo = contar_lineas_codigo(ruta_archivo)
    
    if num_lineas_codigo is not None:
        print(f'Número de líneas de código en {ruta_archivo}: {num_lineas_codigo}')


main()
#por ejemplo si digitamos "Problema1.py" nos arrojara que el numero de lineas es de 39
