'''
RETO PARA RESOLVER:

Programa que pide la edad de una persona e informa de 4 posibilidades:

Si la edad es mayor o igual que 25: "Es un adulto."
Si la edad es mayor o igual que 70: "Es un anciano."
Si la edad es mayor o igual que 14: "Es un joven."
Sino (si la edad es menor de 14): "Es un niño."

Esta vez lo vamos a hacer empezando por la condición excluyente
de ser el menor, y no de ser el más mayor como en el anterior reto.
'''
edad = int(input('Ingrese su edad: \n'))
if(edad >0 and edad < 14):
    print("Es un niño.")
elif(edad >= 14 and edad < 25):
    print("Es un joven.")
elif(edad >= 25 and edad < 70):
    print("Es un adulto.")
elif(edad>=70):
    print("Es un anciano.")
else:
    print("Edad inválida")