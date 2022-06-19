# 1. Importamos libreria Random

import random

# 2. Escribimos el Código

print('Juego: "Adivina el número"\n')

while True:
    try:
        n = int(input('Ingresa un numero entero positivo: '))
    except ValueError:
        print('Incorrecto! Debes ingresar un número entero.\n')
    else:
        num_adivinar  = random.randint(1,n)

        try:
            num_ingresado = int(input('Adivina el número entero elegido al azar entre 1 y el numero ingresado: '))
        except ValueError:
            print('Incorrecto. Debe ingresar un número entero.\n')
        
        else:
            if num_ingresado < num_adivinar:
                print('¡Demasiado pequeño!')
            elif num_ingresado > num_adivinar:
                print('¡Te pasaste!')
            elif num_ingresado == num_adivinar:
                print('¡Adivinaste!')

                break
# FIN






        

        