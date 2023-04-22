#Calcular el producto de todos los n números ingresados, el producto de los pares y el producto de los impares
cantidad = input("Ingrese la cantidad de números a trabajar: \n")
if(cantidad.isalpha()):
    print("Error!, Debe ingresar una cantidad númerics, no letra")
elif(not cantidad):
    print("Error!, Debe ingresar un valor")
else:
    cantidad = int(cantidad)
    while(cantidad<=0):
        print("Error, debe ingresar un número mayor a cero")
        cantidad = int(cantidad)
cantidad = int(cantidad)
cantidadPar=0
cantidadImpar=0
prodNumIngresados=1
prodNumParIngresados=1
prodNumImparIngresados=1

for i in range(1, cantidad+1):
    numero = input(f"Ingresa el número: {i} \n")
    numero = int(numero)
    prodNumIngresados = prodNumIngresados*numero 
    if(numero%2==0):
        cantidadPar = cantidadPar+1
        prodNumParIngresados=prodNumParIngresados*numero
    else:
        cantidadImpar=cantidadImpar+1
        prodNumImparIngresados=prodNumImparIngresados*numero
print(f"El producto de los {cantidad} números ingresados es: {prodNumIngresados}")
if(cantidadPar>=1):
    print(f"El producto de los {cantidadPar} números pares ingresados es: {prodNumParIngresados}")
    if(cantidadImpar>=1):
        print(f"El producto de los {cantidadImpar} números impares ingresados es: {prodNumImparIngresados}")



