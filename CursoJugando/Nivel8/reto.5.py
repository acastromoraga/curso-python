'''
Programa que comprueba cuántas veces está un número en una lista
'''
cantidad = 0
lista = [28,36,43,52,61,43,75,84,43,97]
numero = 43
for i in lista:
    if (i == numero):
        cantidad+=1
print(f"El número {numero} se encuentra {cantidad} veces ")
