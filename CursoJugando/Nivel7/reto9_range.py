numero = int(input("Ingresa un valor entre 8 y 20: \n"))

while (numero in range(8,21)):
    print("Correcto!, estamos en el rango")
    numero = int(input("Ingresa un valor entre 8 y 20: \n"))
else:
    print("Incorrecto!, No estamos en el rango")