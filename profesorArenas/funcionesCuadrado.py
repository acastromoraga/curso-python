def perimetro(lado):
    if(lado>0):
        perim=lado*4
    return perim

def area (lado):
    if(lado>0):
        area=lado**2
    return area

def diagonal(lado):
    if(lado>0):
        diagonal=round((lado**2+lado**2)**0.5,2)
    return diagonal

lado = float(input("Ingrese el lado de un cuadrado: \n"))
perimetro = perimetro(lado)
area = area(lado)
diagonal = diagonal(lado)
print(f"El perimetro es: ", perimetro)
print(f"El area es: ", area)
print(f"La diagonal es: ",diagonal)