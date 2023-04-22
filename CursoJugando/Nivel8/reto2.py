'''
Programa que te pide 5 numeros y los va sumando.
Al final te muestra el resultado

ingreso = True
cantidad = 5
suma = 0
while ingreso:
    numero = int(input("Ingresa un número: \n"))
    suma = suma + numero
    cantidad -= 1
    if cantidad == 0:
        print("Terminó el juego")
        ingreso = False
print(f"Suma total: {suma}")

'''
suma = 0
for cantidad in range (5):    
    numero = float(input("Ingresa un número: \n"))
    suma = suma + numero
print(f"Suma total: {suma}")
