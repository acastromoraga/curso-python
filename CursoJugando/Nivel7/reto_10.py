colores = ['rojo','azul','verde','amarillo','negro']
puntos = 0
jungando = True
print("****Ruta de colores*****")
print("Adivina los 5 colores de la ruleta")
print("Consigue puntos hasta que falles")

while jungando:
    color = (input("Dime un color")).lower()
    if (color in colores):
        puntos += 1
        print("Haz acertado a uno de los colores")
        print(f" tienes: {puntos} puntos")
    else:
        print("El loco no estixte en la lista")    
        print(f" Haz conseguido: {puntos} puntos")
        jungando = False