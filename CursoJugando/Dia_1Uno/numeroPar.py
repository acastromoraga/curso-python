numero = input("Ingresa un número: \n")
if(numero.isalpha()):
    print("Usted ha ingresado un caracter tipo letra")
else:
    numero = int(numero)
    if (numero != 0 and numero%2 == 0):
        print('El número ingresado es par!!')
        print("Adios!!!")
    elif (numero%2 != 0):
        print('El número ingresado es impar!!')
        print("Adios!!!")
    elif numero==0:
        print('El número ingresado es cero!!')
        print("Adios!!!")
    else:
        print('El caracter ingresado es un caracter!!')
        print("Adios!!!")
