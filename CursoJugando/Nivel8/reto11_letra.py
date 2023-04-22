'''
Haz un juego que te pide que adivines una letra, y te pide letras constantemente
hasta que la adivines, y entonces se para.

Se puede probar con todas las letras menos con la "w" en cuyo caso se muestra que
esa letra no está permitida y se para el programa.
'''

letraAdivina = "j"
letraProhibida = "w"
adivina = True

while adivina:
    ingreso = input("Ingresa una letra: \t").lower()

    if ingreso != letraAdivina or ingreso == letraProhibida:
        if ingreso == letraProhibida:
            print(f"Haz ingresado la letra prohibida: {letraProhibida}, juego terminado!!")
            break
        print("Sigue participando!!")
    else:
        print("Haz ganado!!")
        adivina = False
