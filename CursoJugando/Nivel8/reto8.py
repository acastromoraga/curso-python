tabla = [1,2,3,4,5,6,7,8,9,10]
numero = int(input("Ingresa un numero: \t"))

for i in range(len(tabla) + 1):
    print(f"La multiplicación de {numero} * {i} = {numero*i}")