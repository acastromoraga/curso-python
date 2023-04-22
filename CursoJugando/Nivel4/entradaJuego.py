'''
Hacer un programa que simula la entrada a una atracción en un parque
de atracciones, y pide la altura en metros y el peso en kilos. Por seguridad
para poder subir tienes que medir más de 1.3 metros o pesar más de 40.5 kilos,
sino, no puedes subir.

Usa el tipo float para la altura y el peso
'''

print("**********Bienvenido**********")
altura = float(input("Ingresa tu altura el metros: \n"))
peso = float(input("Ingresa tu peso: \n"))

if(altura > 1.3 or peso > 40.5):
    print("Puedes entrar!!!")
else:
    print("No puedes entrar!!!")