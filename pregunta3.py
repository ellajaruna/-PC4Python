# 1. Se instala la libreria pip install pyfiglet en el Visul Studio Code 
# escribir 'pip install pyfiglet' y dar ENTER

# 2. Importamos random
import random

# 3. Importamos Figlet

from pyfiglet import Figlet
figlet = Figlet() 

# 4. Mi código

fuente = str(input('Ingrese el nombre de una fuente: '))

texto = str(input('Ingrese un texto: '))

if fuente in figlet.getFonts():
    figlet.setFont(font=fuente)
    print(figlet.renderText(texto))
     
else:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(texto))
         
# FIN

