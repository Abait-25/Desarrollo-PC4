"""
Empleando el ejercicio visto en clase de Procesamiento con Ficheros. Supongamos que el precio
brindado en el archivo “ventas.csv” ha sido dato en dolares. Deberá solarizar el precio según la
fecha de compra, para esto deberá leer la información almacenada de tipo de cambio de la base
mongodb o sqlite (elegir una). Finalmente mostrar el precio total en dolares y soles por cada producto.
"""

import csv
import sqlite3

archivo_ventas = 'ventas (2).csv'
archivo_sqlite_db = 'base.db'

def obtener_tipo_cambio(fecha):
    conn = sqlite3.connect(archivo_sqlite_db)
    cursor = conn.cursor()
    cursor.execute('SELECT venta FROM sunat_info WHERE fecha = ?', (fecha,))
    resultado = cursor.fetchone()
    conn.close()
    tipo_cambio = resultado[0] if resultado else None
    print(f'Tipo de cambio para {fecha}: {tipo_cambio}')  # Mensaje de depuración
    return tipo_cambio

def procesar_ventas():
    totales_dolares = {}
    totales_soles = {}

    with open(archivo_ventas, mode='r') as file:
        lector = csv.reader(file)
        for fila in lector:
            if len(fila) < 4:
                continue  # Omitir filas con datos incompletos

            fecha, producto, cantidad, precio_dolares = fila
            cantidad = int(cantidad)
            precio_dolares = float(precio_dolares)
            total_dolares = cantidad * precio_dolares

            if producto not in totales_dolares:
                totales_dolares[producto] = 0
                totales_soles[producto] = 0

            totales_dolares[producto] += total_dolares

            tipo_cambio = obtener_tipo_cambio(fecha)
            if tipo_cambio:
                total_soles = total_dolares * tipo_cambio
                totales_soles[producto] += total_soles

    # Mostrar resultados
    for producto in totales_dolares:
        print(f"Producto: {producto}")
        print(f"Total en dólares: ${totales_dolares[producto]:,.2f}")
        print(f"Total en soles: S/{totales_soles[producto]:,.2f}")
        print('----------------------')

procesar_ventas()
