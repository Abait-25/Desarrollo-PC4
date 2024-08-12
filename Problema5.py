"""
Escriba un programa que realice las siguientes tareas (Puede usar clases y/o funciones,
también puede usar un menú para organizar su programa):
- Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre
tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
- Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, donde “n” es el número introducido, y la muestre por
pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de
ello.
- Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero
no existe debe mostrar un mensaje por pantalla informando de ello.
"""

import os

def generar_tabla_multiplicar(n):
    nombre_archivo = f'tabla-{n}.txt'
    with open(nombre_archivo, 'w') as archivo:
        for i in range(1, 11):
            archivo.write(f'{n} x {i} = {n * i}\n')
    print(f'Tabla de multiplicar del {n} guardada en {nombre_archivo}')

def mostrar_tabla_multiplicar(n):
    nombre_archivo = f'tabla-{n}.txt'
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        print(f'Tabla de multiplicar del {n}:\n{contenido}')
    else:
        print(f'El archivo {nombre_archivo} no existe.')

def mostrar_linea_tabla_multiplicar(n, m):
    nombre_archivo = f'tabla-{n}.txt'
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                if 1 <= m <= len(lineas):
                    print(f'Línea {m} de la tabla de multiplicar del {n}: {lineas[m - 1].strip()}')
                else:
                    print(f'La línea {m} no existe en el archivo {nombre_archivo}.')
        except Exception as e:
            print(f'Error al leer el archivo: {e}')
    else:
        print(f'El archivo {nombre_archivo} no existe.')

def main():
    while True:
        try:
            n = int(input('Introduce un número entero entre 1 y 10 para generar la tabla de multiplicar: '))
            if 1 <= n <= 10:
                break
            else:
                print('El número debe estar entre 1 y 10.')
        except ValueError:
            print('Por favor, introduce un número entero válido.')

    generar_tabla_multiplicar(n)

    while True:
        try:
            n = int(input('Introduce un número entero entre 1 y 10 para mostrar la tabla de multiplicar: '))
            if 1 <= n <= 10:
                break
            else:
                print('El número debe estar entre 1 y 10.')
        except ValueError:
            print('Por favor, introduce un número entero válido.')

    mostrar_tabla_multiplicar(n)


    while True:
        try:
            n = int(input('Introduce un número entero entre 1 y 10 para mostrar una línea de la tabla de multiplicar: '))
            if 1 <= n <= 10:
                m = int(input('Introduce el número de la línea que deseas mostrar: '))
                if 1 <= m <= 10:
                    break
                else:
                    print('El número de línea debe estar entre 1 y 10.')
            else:
                print('El número debe estar entre 1 y 10.')
        except ValueError:
            print('Por favor, introduce un número entero válido.')

    mostrar_linea_tabla_multiplicar(n, m)


main()
