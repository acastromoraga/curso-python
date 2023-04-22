'''Programa que te dice las vocales que tiene una palabra'''

palabra =input("Introduce una palabra: \n")
vocales = "aeiouáéíóü"
indice = 0
cantidadVocales = 0
largoPalabra = len(palabra)

while indice < largoPalabra:
    if( palabra[indice] in vocales):
        cantidadVocales +=1
    indice+=1
print(f"El número de vocales es: {cantidadVocales}")