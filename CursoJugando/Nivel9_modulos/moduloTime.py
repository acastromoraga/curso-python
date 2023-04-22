import time

inicio  = time.time()

while True:
    print("Estamos jugando....")

    final = time.time()
    transcurrido = final -inicio
    if((transcurrido) >= 5 ):
        break
print(f"Fin del juego, tiempo total del juego {transcurrido}")