from math import pi

def perimetroCircunferecia(radio):
    if(radio>0):
        perimetro = 2*pi*radio
    return perimetro

def areaCircunferencia(radio):
    if(radio>0):
        area = pi*radio**2
    return area

radio = float(input("Ingrese el radio de una circunferencia: \n"))
perimetro = perimetroCircunferecia(radio)
areaCircun = areaCircunferencia(radio)
print("El perimetro es: ", perimetro)
print("El area de la circunferencia es: ", areaCircun)