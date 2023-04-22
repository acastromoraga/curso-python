'''
Programa que compara si un elemento está en un lista y nos dice en que posición se encuentra

'''

lista = [2,3,90,23,45,87,54,11,38]

elemento  = 54

for i in range(len(lista)):
    if lista[i]==elemento:
        print(f" El elemento {elemento} se encuentra en la lista en la posición {(i+1)} ")