"""
"""
import requests
import sqlite3
from pymongo import MongoClient

url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
fecha_inicio = '2023-01-01'
fecha_fin = '2023-12-31'

def obtener_datos_sunat(fecha_inicio, fecha_fin):
    try:
        respuesta = requests.get(url, params={'start_date': fecha_inicio, 'end_date': fecha_fin})
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.RequestException as e:
        print(f'Error al consultar el API: {e}')
        return None

def almacenar_sqlite(datos):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')
    for registro in datos['data']:
        cursor.execute('''
            INSERT OR REPLACE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
        ''', (registro['fecha'], registro['compra'], registro['venta']))
    conn.commit()
    conn.close()

def almacenar_mongodb(datos):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['sunat_db']
    collection = db['sunat_info']
    collection.drop()  # Eliminar la colección si ya existe
    collection.insert_many(datos['data'])

def mostrar_contenido_sqlite():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sunat_info')
    filas = cursor.fetchall()
    for fila in filas:
        print(f'Fecha: {fila[0]}, Compra: {fila[1]}, Venta: {fila[2]}')
    conn.close()

def main():
    datos_sunat = obtener_datos_sunat(fecha_inicio, fecha_fin)
    if datos_sunat:
        almacenar_sqlite(datos_sunat)
        almacenar_mongodb(datos_sunat)
        print('Datos almacenados en SQLite y MongoDB.')
        print('Contenido de la tabla en SQLite:')
        mostrar_contenido_sqlite()


main()

