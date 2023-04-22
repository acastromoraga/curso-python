num=2
vocal = 'u'
intentos = 0
bonos = 100
acierto= True
while acierto:
    aciertoVocal = input('Ingresa una vocal: \n')
    aciertoNum = int(input('Ingresa una número: \n'))
    if(aciertoNum == num and aciertoVocal == vocal):
        print("Haz acertado, Bienvenido al juego")
        acierto = False
        intentos+=1
        print(f"Intentos: {intentos}")
        break
    elif(aciertoNum != num and aciertoVocal != vocal):
        print("No haz acertado a ninguno")
        bonos -= 5
        intentos+=1
        print(f"Intentos: {intentos}")
        print(f"Bonos: {bonos}")
    elif(aciertoNum == num or aciertoVocal != vocal):
        print("No haz acertado a ninguno")
        bonos -= 2
        intentos+=1
        print(f"Intentos: {intentos}")
        print(f"Bonos: {bonos}")
    elif(aciertoNum != num or aciertoVocal == vocal):
        print("No haz acertado a ninguno")
        bonos -= 2
        intentos+=1
        print(f"Intentos: {intentos}")
        print(f"Bonos: {bonos}")
    
