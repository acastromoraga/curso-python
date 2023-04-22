numero= input("Ingresa un numero: \n")
numero = int(numero)
cantidad = 0
while True:
    if cantidad<numero:
        cantidad+=1
        print(cantidad)
        continue
    else:
        break