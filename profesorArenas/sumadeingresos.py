cantidad = input("Ingrese la cantidad de números a traabajar: \n")
if(cantidad.isalpha()):
    print("Debe ingresar un número entero")
elif(not cantidad):
    print("Debe ingresar un valor")
else:
    cantidad=int(cantidad)
    while(cantidad<=0):
        print("Error!, solo deden ser número enteros")
        cantidad = input("Ingrese la cantidad de números a trabajar: \n")
cantidad=int(cantidad)
suma=0
sumaImpar = 0
sumaPar = 0
cantidadPar=0
cantidadImpar=0
for i in range(1, cantidad+1):
    numero=input(f"Digite el número: {i}\n")
    numero=int(numero)
    suma = suma + numero
    if(numero%2==0):
        cantidadPar=cantidadPar+1
        sumaPar = sumaPar + numero
    else:
        cantidadImpar=cantidadImpar+1
        sumaImpar = sumaImpar + numero
print(f"La suma total de los números es: {sumaPar}")
print(f"La suma de los {cantidadPar} números pares ingresados de es: {sumaPar}")
print(f"La suma de los {cantidadImpar} nuúmeros impares de es: {sumaImpar}")
