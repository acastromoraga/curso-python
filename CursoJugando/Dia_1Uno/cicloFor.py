numero = input("Ingresa un numero: \n")
if(numero.isalpha()):
    print("Debe ingresar un número no letra")
elif (not numero):
    print("debe ingresar un valor")
else:
    numero = int(numero)
    print(f"Numero ingresado: {numero}")

    for i in range(numero):
        print("Hola Mundo")

##Es primo
