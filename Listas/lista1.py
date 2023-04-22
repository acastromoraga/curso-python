#declaracion de lista unidimensionales
numeros = []
#lista con los números
numeros = [1,4,6]

#Listas bidireccionales
lista_bidireccional = [[1,4], [6,6]]

#Recorriendo una lista con for
nombres = ["Ana", "Luis","palabra 1","palabra 2","palabra 3"]

print("Recorrido forma 1")
for elemento in nombres:
    print(elemento)

print("Recorrido forma 2")
for i in range (len(nombres)):
    print(nombres[i])

#Metodo para agregar una variable
pruebas=[]
pruebas.append("palabra agregada 1")
pruebas.append(34)
pruebas.append(False)
pruebas.append(3.3456)

for i in range(len(pruebas)):
    print(pruebas[i])

#pop(): este metodo nos permite eliminar el ultimo elemento de la lista, que ademas, puede ser asignado a una
#variable

mi_lista= [1,4,6,7,8,9]
elemento_eliminado = mi_lista.pop()
print(elemento_eliminado)

#Eliminamos el ultimo valor sin asignaion
mi_lista.pop()

for i in range(len(mi_lista)):
    print(mi_lista[i])
elemEli = str(mi_lista.pop(2))
print("Elimento eliminado: " + elemEli)

#List de familia
familias = ["tio", "primo", "mamá", "papá", "hijo"]

for i in range (len(familias)):
    print("Famlia: "  + familias[i])

familias.remove("mamá")
for i in range (len(familias)):
    print("Famlia: "  + familias[i])

#extend(): este metodo tambien nos permite agregar elementos a la lista, pero a diferencia del metodo append,
#pasamos como argumento algo que podemos recorrer (como por ejemplo otra lista), agregando cada uno de
#los elementos.

lista_1 = [1,3,5]
lista_2 = [2,4]
lista_3 = [6,7,8]
lista_1.extend(lista_2)
print(lista_1)
for i in range(len(lista_1)):
    print(lista_1[i])

#reverse(): nos permite invertir los elementos de la lista.
for i in range(len(lista_1)):
    print(lista_1[i])
lista_1.reverse()

print("reverse")
for i in range(len(lista_1)):
    print(lista_1[i])

#index(e): retorna el entero que representa la posicion de la primera aparicion del elememto e en la lista. Si e
#no existe en la lista, obtendremos un ValueError.

lista_personas = ["Ana","jose","Leo","pao"]
lista_mun = [1,3,4,5,68]

pos1 = lista_personas.index("jose")
pos2 = lista_personas.index("pao")
print("pos: ",pos1)
print("pos: ",pos2)
pos3 = lista_mun.index(68)
pos4 = lista_mun.index(5)
print("pos: ",pos3)
print("pos: ",pos4)

#count(e):retorna la cantidad de veces que e se encuentra en la lista.
numerica = [1,2,3,3,3,3,5,6,6,7,7,7,7,7,7]
num3 = numerica.count(3)
print("cantidad 3: ", num3)
num6 = numerica.count(6)
print("cantidad 6: ", num6)
num7 = numerica.count(7)
print("cantidad 7: ", num7)

#Indexing: una vez inicializada la lista, podemos acceder al i-esimo elemento de la misma manera en que lo
#haciamos con los strings

nueva = [2,5,7,9,12,55]
a = nueva[3]
print(a)
b = nueva[-2]
print(b)
c = nueva[0]
print(c)
print("Reemplazo: ")
nueva[4] 

#indexing a listyas bidimensionales

matriz = [['a','b','c','d'],
          ['f','g','h','i'],
          ['j','k','l','m']
        ]

var1 = matriz[0][0]
var2 = matriz[0][1]

#slicing una vez inicializada la lista, podemos acceder a partes d ela lista, de la misma forma en que lo haciamos con los string

listaNum =[2,4,6,8,10,12]

#todos los elementos
c = listaNum[:]

#desde la posicion 2 a la 4
d = listaNum[2:5]

#desde el inicio hasta la posicion 3

e = listaNum[2:4]

#desde la posicion 2 hasta el final

f = listaNum[2:]

#desde la posicion 1 a la -3
g = listaNum[1:-2]

#cambiar los valores de la posicion 1 a la 2
listaNum[1:3] = ['a','b']
for i in range (len(listaNum)):
    print(listaNum[i])

print(listaNum)

var3 = matriz[0][:]
print(var3)

#obtener los primeros 3 valores de la matriz
var4=matriz[0][:3]


#union
listaUno = [1,2,3]
listaDos = [5,7,9]
union = listaUno + listaDos
print(union)