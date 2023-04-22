'''
Calcula el valor del perímetro de una elipse, cuyos semiejes son 3 y 7.
'''
from math import pi, sqrt

semi_eje_1 = float(input("Ingresa el primer semi eje: \t"))
semi_eje_2 = float(input("Ingresa el segundo semi eje: \t"))

suma_cuadradra_div = (semi_eje_1**2 + semi_eje_2**2)/2
perimetro = 2* pi * sqrt(suma_cuadradra_div)

print(f"El perimetro de la elipce es: {perimetro}")