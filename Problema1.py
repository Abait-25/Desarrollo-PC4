"""
Solicite al usuario por línea de comando un valor de “n” el cual representa la cantidad
de bitcoins que posee el usuario.
- Consulte la API del índice de precios de Bitcoin de CoinDesk en el siguiente link
(https://api.coindesk.com/v1/bpi/currentprice.json), la cual retornará un objeto JSON,
entre cuyas claves anidadas encontrará el precio actual de Bitcoin como un número
decimal. Asegúrese de detectar cualquier excepción, como el siguiente código:
import requests
try:
...
except requests.RequestException:
...
- Muestra el costo actual de “n” Bitcoins en USD con cuatro decimales, usando , como
separador de miles.

"""

import requests

def obtener_precio_bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status() 
        datos = respuesta.json()
        return datos['bpi']['USD']['rate_float']
    except requests.RequestException as e:
        print(f"Error al consultar la API: {e}")
        return None

def calcular_costo_total(bitcoins, precio_por_bitcoin):
    return bitcoins * precio_por_bitcoin

def main():
    try:
        n = float(input("Ingrese la cantidad de bitcoins que posee: "))
        
        precio_bitcoin = obtener_precio_bitcoin()
        
        if precio_bitcoin is not None:
            
            costo_total = calcular_costo_total(n, precio_bitcoin)
              
            print(f"El costo actual de {n:,.4f} Bitcoins en USD es: ${costo_total:,.4f}")
        else:
            print("No se pudo obtener el precio de Bitcoin.")
    except ValueError:
        print("Por favor, ingrese un número válido para la cantidad de bitcoins.")

