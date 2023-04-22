#RETO PARA RESOLVER:
#Haz un programa que calcule el año en el que has nacido.
#Pide el año en el que estamos.
#Pide cuántos años tienes o vas a cumplir este año.
#Calcula el año en el que has nacido.
#Muestra el resultado con un 'print'

annioHoy = int(input('Ingresa el año actual: \n'))
print(type(annioHoy))
edad = int(input('Ingresa tu edad: \n'))
print(type(edad))
annio_nacimiento = annioHoy - edad
print(f'Año de nacimiento: {annio_nacimiento}')