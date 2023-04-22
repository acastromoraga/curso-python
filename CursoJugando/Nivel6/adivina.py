adivina = 5
contador = 0
ingreso = int(input("Ingresa un número para adivinar: \n"))
while(ingreso != adivina):
    contador = contador +1
    print(f"Intentos: {contador}")
    ingreso = int(input("Ingresa un número para adivinar: \n"))
else:
    print("Fin del juego!")