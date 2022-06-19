# 1. Importamo re
import re

# 2. Texto
texto = '@robot9! @robot4& I have a good feeling that the show is going to be amazing! @robot9$ @robot7%'

# 3. Regex
patron = r"@robot\d\W"

# 4. Imprimimos los valores detectados
print(re.findall(patron, texto))

# FIN


