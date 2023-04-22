mi_tupla = (1,2,3,4)
print(type(mi_tupla))

mi_tupla2= ("Ale", 56, False)
print(mi_tupla2)
print(mi_tupla2[1])

#imprimir de derecha a izquierda
print(mi_tupla2[-1])

#son inmutables
##mi_tupla2[1] = 'hoa'
print(mi_tupla2)

# consultar en tuples de anidados
mi_tupla3= (1,2,(4,3), 7)
print(mi_tupla3[2][0])

#casting de tuple a list
mi_tupla3= (1,2,(4,3), 7)
mi_tupla3 = list(mi_tupla3)
print(type(mi_tupla3))

#asignar valores a variables a partir de tuple, esto ocurre cuando siempre exista l amisa cantidad de objetos, esto se puede hacer con las listas y direccionarios
t= (1,3,6,1)
##x,y,z = t
##print(x,y,z)
print(len(t))# el largo de la tupla

#cantidad deveces aparece
print(t.count(1))

#cual es el valor de acuerdo al indice
print(t.index(6))