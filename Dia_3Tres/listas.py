mi_lista = ["a","b","c"]
print(type(mi_lista))

mi_seg_lista = ["Alejandro", "castro", 38, False]
print(type(mi_seg_lista))
largo = len(mi_lista)
largo_Seg =len(mi_seg_lista)
print(largo)
print(largo_Seg)

#indexar una lista
resultado = mi_seg_lista[2]
print(resultado)
resultado = mi_seg_lista[0:2]
print(resultado)
print(mi_lista + mi_seg_lista)
mi_tercera_lista = mi_lista + mi_seg_lista
print(mi_tercera_lista)

#cambiar un caracter
mi_tercera_lista[3]='Ana'
print(mi_tercera_lista)
#agregar un elemento a la lista
mi_tercera_lista.append("agregado_1")
print(mi_tercera_lista)

#eliminar un elemento de la lista, si no se pone argumento, elimina el último elemento, a no ser de indicar el indice
mi_tercera_lista.pop()
print(mi_tercera_lista)

mi_tercera_lista.pop(2)
print(mi_tercera_lista)

#almacenar el elemento eliminado y guardarlo en una variable
primerEli= mi_tercera_lista.pop()
print(mi_tercera_lista)
print(primerEli)

seg_eliminado =mi_tercera_lista.pop(2)
print(mi_tercera_lista)
print(seg_eliminado)

