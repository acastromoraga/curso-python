'''Haz un programa que calcula el área de un círculo.
La fórmula es: 2 por pi por radio al cuadrado.
'''
##import math
from math import pi
radio = float(input("Ingresa el radio de la circunferencia en cm \t"))

perimetro = 2 * pi * radio
area = pi * radio**2

print(f"El perimetro de la circunferencia de radio {radio} es : {perimetro} cm")
print(f"El area de la circunferencia de radio {radio} es : {area} cm2")