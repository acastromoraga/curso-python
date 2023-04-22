numero = input("Ingresa un número: \n")
print(type(numero))
if(numero.isalpha()):
    print("Error, lo ingresado es una letra")
    numero = input("Ingresa un número: \n")
elif(not numero):
    print("Error, No ingresado nada")
    numero = input("Ingresa un número: \n")
numero=int(numero)
while(numero<=0):
    print("Error, lo ingresado es cero")
    numero = input("Ingresa un número: \n")
    numero=int(numero)

numero=int(numero)
sumaPar=0
sumaImpar=0
for i in range(1, numero+1):
    if(i%2==0):
        sumaPar=sumaPar + i
    else:
        sumaImpar=sumaImpar+i
print(f"La suma de los pares del 1 al {numero} es {sumaPar}")
print(f"La suma de los impares del 1 al {numero} es {sumaImpar}")