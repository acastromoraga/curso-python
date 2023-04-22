mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

#otro forma de crear un set
otro_set = {1,2,3,4,5,6,7}
print(type(otro_set))

#set con valores repetidos

set_repetidos = {1,1,1,1,5,6,7,7,8}
print(set_repetidos)
print(len(set_repetidos))
#no acepta ni listas ni diccionarios, pero si tuples, ya que son inmutables
print(2 in set_repetidos)

#unir set
s2 = mi_set.union(set_repetidos)
print(s2)

#add agregar 
s2.add(40)
print(s2)
s2.remove(40)
print(s2)
