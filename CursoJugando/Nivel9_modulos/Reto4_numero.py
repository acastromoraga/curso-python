from random import randint
from random import choice
aleatorio = randint(1,100)
cantidadIntentos = 7
arriba = ['Te pasaste', 'Muy arriba','Te subiste mucho', 'El numero es menor']
abajo = ['muy bajo', 'el numero es más alto', 'te bajaste mucho', 'El número es mayor']

while cantidadIntentos>=0:
    intento = int(input(f"Ingresa un número para adivinar, te quedan {cantidadIntentos} \t"))

    if(intento == aleatorio):
        print(f"Le has apuntado quedando : {cantidadIntentos} intento")
        break
    else:
        print("No has apuntado, sigue intentando")
        if(intento > aleatorio):
            print(choice(arriba))
        else:
            print(choice(abajo))
    cantidadIntentos -= 1
print(f"El número era: {aleatorio}")    