# 1. Se instala la libreria pip install requests en el Visul Studio Code 
# escribir 'pip install requests' y dar ENTER

# 2. Importamos requests

import requests

# 3. URL

url = "https://api.coindesk.com/v1/bpi/currentprice.json" 

r = requests.get(url)  # solicita la información a la url

r.status_code  # 200 sognifica OK

# 4. Respuesta en formato Json

data = r.json()

# 5. Localizamos Precio del Bitcoin en USD

data 

data.keys()

bitcoin_USD = data['bpi']['USD']['rate_float']

print(f'Precio actual del Bitcoin: ${bitcoin_USD}\n')

# 6. Mi código

while True:
    try:
        n = int(input('Ingrese una cantidad de bitcoins: '))

        dolares = bitcoin_USD * n

        print(f'${dolares:,.4f}')

        break

    except:
        print('¡Incorrecto!\n') 

# FIN