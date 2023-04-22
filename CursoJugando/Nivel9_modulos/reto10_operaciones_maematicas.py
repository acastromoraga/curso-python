from random import randint,choice
from time import time

puntos = 0

inicio_tiempo = time()

while True:
    num1 = randint(1,10)
    num2 = randint(1,10)
    operacion = choice(["+","*"])

    if operacion == "+":
        print(f"Calcular: {num1} + {num2}")
        resultado = num1 + num2
    else:
        print(f"Calcular: {num1} * {num2}")
        resultado = num1 * num2    
    respuesta = int(input("Ingrese respuesta: \t"))

    if respuesta == resultado:
        print(f"Correcto!, tienes: {puntos} puntos")
        puntos +=1
    else:
        print(f"Error, fin del juego, obtuviste: {puntos} puntos")
        break

    tiempo_avanzado = time()
    tiempo_Total = tiempo_avanzado - inicio_tiempo

    if tiempo_Total>= 10:
        (print(f"Fin del juego tiempo jugado: {tiempo_Total},, obtuviste: {puntos} puntos"))
        break