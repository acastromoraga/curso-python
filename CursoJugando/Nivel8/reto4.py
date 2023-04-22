'''
Programa que pide un número al usuario. Si ese número más alg´n número de la lista
dada es igual a 100, el programa dice que el número cumple con la condicion
'''

lista = [28, 36, 43, 52, 61,75,84,97]
ingreso  = True
suma = 0

while ingreso:
    numero = int(input("Ingresa un número: \t"))
    for i in lista:
        suma = numero + i
        if(suma == 100):
            print(f"{numero} cumple con la condición más el número {[i]}")
            ingreso = False
        