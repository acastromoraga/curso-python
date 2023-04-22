operacion = input("Ingrese la operación aritmética que desea realizar: \n Suma ingresa 1\n Resta ingresa 2\n Multiplicación ingresa 3\n División ingresa 4: \n")
if(operacion == "1" or operacion == "2" or operacion == "3" or operacion == "4"):
    print("Bienvenido!!")
    numero1 = input("Ingrese un múmero: \n")
    if(numero1.isalpha()):
        print("Debe ingresar un dígito")
    else:
        numero1 = int(numero1)
    numero2 = input("Ingrese un segundo múmero: \n")
    if(numero2.isalpha()):
        print("Debe ingresar un dígito")
    else:
        numero2 = int(numero2)
    if(operacion==1):
        suma = numero1 + numero2
        print(f"La suma de {numero1} + {numero2} es: {suma}")
    elif(operacion==2):
        resta = numero1 - numero2
        print(f"La resta de {numero1} - {numero2} es: {resta}")
    elif(operacion==3):
        multi = numero1 * numero2
        print(f"La multiplicación de {numero1} * {numero2} es: {multi}")
    else:
        div = numero1 / numero2
        div = round(div,2)
        print(f"La división de {numero1} / {numero2} es: {div}")

else:
    print("Ingrese una opción correcta!!")