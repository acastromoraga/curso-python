'''Haz un programa que muestra si los números de una lista son positivos o negativos,
a excepción del cero que se lo salta y no muestra nada.

Utiliza la sentencia "continue".

numeros = [1,4,-3,5,0,7,-2,6]
'''
numeros = [1,4,-3,5,0,7,-2,6]

for i in numeros:
    if i < 0:
        print(f"Negativo: {i}")
    elif i > 0:
        print(f"Psitivo: {i}")
    else:
        continue