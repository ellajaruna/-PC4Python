# 1. Importamos re

import re

# 2. Texto
lista = ["n.john.smith@gmail.com","87victory@hotmail.com","!#mary-=@msca.net"]

# 3. Regex
patron = r'\w*\W*\w*\W*@w*\W*\w*\W*.com'

# 4. Mi código
for correo in lista:
    if re.findall(patron, correo):
        print(f'The email {correo} is a valid email')
        continue
    print(f'The email {correo} is invalid')

# FIN