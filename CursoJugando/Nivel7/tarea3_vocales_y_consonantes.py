palabra = input("Ingresa una frase : \n")
largoPalabra = len(palabra)
indice = 0
cantidadVocales = 0
cantidadConsonantes = 0
vocales = "aeiouáéíóü"

while indice < largoPalabra:
    if palabra[indice] in vocales:
        cantidadVocales +=1
    else:
        cantidadConsonantes+=1
    indice+=1
print(f"Cantidad de vocales: {cantidadVocales}")
print(f"Cantidad de consonantes: {cantidadConsonantes}")
print(f"Cantidad total caracteres: {largoPalabra}")

