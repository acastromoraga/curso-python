'''
Programa que muestra las letras de una palabra a excepción de la h
'''

palabra = "zanahoria"

for i in palabra:
    if i == "h":
        continue
    else:
        print(i)