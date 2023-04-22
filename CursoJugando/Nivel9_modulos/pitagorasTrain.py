'''
RETO PARA RESOLVER:

Haz un programa que calcule el valor de la hipotenusa de un triángulo rectángulo, dados sus lados.

La fórmula es: c al cuadrado es igual a la raiz cuadrada de
a al cuadrado más b al cuadrado.
'''
from math import sqrt
lado_a = float(input("Ingresa el valor del lado a del triangulo: \t"))
lado_b = float(input("Ingresa el valor del lado b del triangulo: \t"))

suma_cuadrado = lado_a**2 + lado_b**2
lado_c =  sqrt(suma_cuadrado)

print(f"El lado de la hipotenusa del cuadrado de lado a: {lado_a} y lado b: {lado_b} es = {lado_c}")