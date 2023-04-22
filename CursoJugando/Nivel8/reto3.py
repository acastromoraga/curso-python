'''
Programa que va pidiendo números y los va sumando hasta que alcanza 100 o más.
Entonces para y muestra el total
'''
ingresos = True
numeros = 0
suma = 0

while ingresos:
    numeros = float(input("Ingresa un número \t"))
    suma = suma + numeros
    if(suma <= 100):
        ingresos = True
    else:
        ingresos = False
        #break
print(f"Suma total con ciclo while: {suma}")

