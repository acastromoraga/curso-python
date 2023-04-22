#Imprimir lo que existe en el indice 0
mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)

#Imprimir lo que existe en el indice 9
mi_texto = "Esta es una prueba"
resultado = mi_texto[9]
print(resultado)

#Imprimir lo que existe en el indice -4
resultado=mi_texto[-4]
print(resultado)

#Imprimir lo que existe en el indice de un caracter
resultado = mi_texto.index("a")
print(resultado)

resultado = mi_texto.index("una")
print(resultado)

resultado = mi_texto.index("u")
print(resultado)

resultado = mi_texto.index("a",5,15)
print(resultado)

#Imprimir lo que existe en el indice de un caracter de derecha a izquierda
resultado = mi_texto.rindex("u")
print(resultado)