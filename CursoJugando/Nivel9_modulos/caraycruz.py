from random import choice
 
moneda = ['cara','sello']
cantSello = 0
cantCara = 0

for i in range(1,101):
    caida = choice(moneda)
    if caida == 'cara':
        cantCara += 1
    else:
        cantSello +=1
print(f" Cantidad de caras : {cantCara} cantidad de sellos: {cantSello}")
