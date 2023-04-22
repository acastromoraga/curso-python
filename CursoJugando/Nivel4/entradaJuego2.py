'''
Hacer un programa que simula la entrada a una atracción en un parque
de atracciones, y pide la altura en metros y el peso en kilos. Por seguridad
para poder subir tienes que medir más de 1.3 metros o pesar más de 40.5 kilos,
sino, no puedes subir.

Usa el tipo float para la altura y el peso
'''

print("**********Bienvenido**********")
altura = float(input("Ingresa tu altura el metros: \n"))
if(altura > 1.3):
    peso = float(input("Ingresa tu peso: \n"))
    if(peso > 40.5):
        print("Puedes entrar!!!")
    else:
        print("No puedes entrar porque no tienes el peso adecuado!!!")
else:
    print("No puedes entrar porque no tienes la altura adecuada!!!")