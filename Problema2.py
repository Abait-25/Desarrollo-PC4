pip install pyfiglet
import random
from pyfiglet import Figlet

def seleccionar_fuente(figlet):
    fuentes = figlet.getFonts()
    fuente = input("Ingrese el nombre de la fuente (o presione Enter para seleccionar una aleatoria): ")
    
    if fuente not in fuentes:
        print(f"La fuente '{fuente}' no es válida. Seleccionando una fuente aleatoria.")
        fuente = random.choice(fuentes)
        print(f"Fuente seleccionada aleatoriamente: {fuente}")
    
    return fuente

def main():
    figlet = Figlet()
    
    fuente_seleccionada = seleccionar_fuente(figlet)
    
    texto = input("Ingrese el texto que desea convertir a arte ASCII: ")
    
    figlet.setFont(font=fuente_seleccionada)
    texto_ascii = figlet.renderText(texto)
    
    print("\nTexto en arte ASCII:")
    print(texto_ascii)

if __name__ == "__main__":
    main()
