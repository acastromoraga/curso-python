probando = True

while probando:
    numero = int(input("Ingresa un numero entre 10 y 20: \n"))
    if( numero in range(10,21)):
        print("Estamos ok!")
    else:
        print("Estamos Nok!, fuera de rango")
        probando = False