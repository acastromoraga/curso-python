frase = input("Ingrese un texto a su elección: ")
letras = []
frase = frase.lower()
print(frase)
letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la seguna letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\n")
cantidadLetras1 = frase.count(letras[0])
cantidadLetras2 = frase.count(letras[1])
cantidadLetras3 = frase.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidadLetras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidadLetras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidadLetras3} veces")

mi_lista = frase.split()
largo = len(mi_lista)
print(mi_lista)
print(f"Tu texto contiene {largo} palabras ")

primeraLetra = frase[0]
largoFrase = len(frase)
ultimaLetra = frase[largoFrase-1]
print(f"La primera letra del texto es: {primeraLetra}")
print(f"La última letra del texto es: {ultimaLetra}")
mi_lista.reverse()
textoInvertido = ' '.join(mi_lista)
print(textoInvertido)
control = "python" in frase
diccionario = {True: "Si se encuentra", False: " No se encuentra"}
##control = str(control)
print(f"Python {diccionario[control]} en la frase: ")

