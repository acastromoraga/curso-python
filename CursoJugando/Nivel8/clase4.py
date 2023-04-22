letras = ['a','f','m','s','v','l']
'''
for letra in letras:
    if letra == "m":
        print(f"Esta la letra en la posicion {[letra]}")
    else:
        print("No esta la letra")
'''
encontrado = False
for i in letras:
    if i == "m":
        encontrado = True
if (encontrado == True):
     print(f"La letra está en la posicion")
else:
    print("La letra No está")