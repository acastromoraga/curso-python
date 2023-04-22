numero = input("Ingrese un número: \n")
if(numero.isalpha()):
    print("Error!! usted no ha ingresado un número")
elif(not numero):
    print("No ha ingresado un valor")
else:
    numero = int(numero)
    if numero<=0:
        print("Numero debe ser mayor a cero")
    else:
        contador = 0
        while contador<numero:
            contador = contador + 1
            print(F"Progresión: {contador}") 
