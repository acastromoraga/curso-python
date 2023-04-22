from random import choice,randint

cachipunAleato = [1,2,3]
jugando = True
opcion = "s"
salir = True

while jugando:
    maquina = choice(cachipunAleato)
    jugadorOpcion = int(input("Elige\n 1-Piedra\n 2-Papel\n 3-Tijeras\n"))

    if (maquina==1):
        if(jugadorOpcion==maquina):
            print("Sacaron ambos Piedra, empate")
        elif(jugadorOpcion==2):
            print("El jugador gana, sacó papel ")
        else:
            print("La máquina gana, sacó Piedra y el jugador tijeras ")
    if (maquina==2):
        if(jugadorOpcion==maquina):
            print("Sacaron ambos Papel, Papel")
        elif(jugadorOpcion==1):
            print("Máquina gana, sacó papel y el jugador piedra")
        else:
            print("Jugador gana, jugador sacó tijeras y la máquina papel")                 
    if (maquina==3):
        if(jugadorOpcion==maquina):
            print("Sacaron ambos Tijeras, Tijeras")
        elif(jugadorOpcion==1):
            print("Jugador gana, Jugador sacó piedra y la maquina tijeras")
        else:
            print("maquina gana, maquina sacó tijeras y el jugador papel")
    while salir:
        opcion = input("Seguir jugando (S/N): \t")
        if ( opcion == "s" or opcion == "S" or opcion == "N" or opcion == "n"):
            if(opcion == "n" or opcion == "N"):
                print("Fin del juego, Adios")
                salir = False
                jugando = False
            else:
                salir = False
                jugando = True
        else:
            print("Oopcion inválida")
    salir = True