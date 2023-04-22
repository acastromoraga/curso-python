'''
Programa que comprueba si un número está dentro de una secuencia
'''

numero = 20

secuencia = range(1, 101)
contador = 0
for i in secuencia:
    if i == numero:
        print(f"Se encuentra el número dentro del rango, posicion {contador}")
        break
    else:
        contador+=1
print("No se encuentra")
     