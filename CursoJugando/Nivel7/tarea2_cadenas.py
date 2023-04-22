cadena = """Muchos años después, frente al pelotón de fusilamiento,
el coronel Aureliano Buendía había de recordar aquella tarde remota
en que su padre lo llevó a conocer el hielo."""
n = 0
longitud = len(cadena)
cantidadN = 0
while n < longitud:
    if cadena[n] == "o" or cadena[n] =="ó":
        cantidadN +=1
    n +=1
print(f"Cantidad de o con tilde y sin tildes es: {cantidadN}")