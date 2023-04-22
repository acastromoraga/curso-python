numero = input("Ingrese un número: \n")
if(numero.isalpha()):
    print("El número ingresado es letra")
elif(not numero):
    print("Debe ingresar un valor")
else:
    numero=int(numero)
    while(numero<=0):
        print("Error!, debe ingresar un número")
        numero = input("Ingrese un número: \n")
        numero = int(numero)
    suma=0
    for i in range(1,numero+1):
        cuadrado=i**2
        suma = suma + cuadrado
    print(f"El resultado de la suma de los cuadrados de: {numero} es {suma}")
