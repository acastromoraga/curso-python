print("Bienvenidos")
jugando = "s"
contador = 0
while jugando =="s":
    print("Seguimos jugando.")
    contador = contador + 1
    jugando = input("¿Quieres seguir jugando (s/n): \n")
print(f"Fin del juego!, jugaste {contador} veces")