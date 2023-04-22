mascotas = ["gato", "perro","canario","cocodrilo"]
print(mascotas)
#Las listas son mutables
mascotas[3]= "tortuga"
print(mascotas)

#las tuplas son mas rápidas que las listas
#las listas son mutables
#las tuplas se usan para datos que no deben ser modificados

dias_semana = ("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo")
dias_entrenamiento = ["Lunes", "Jueves", "Viernes"]

lista_Inicio = []
print(lista_Inicio)
lista_Inicio = lista_Inicio + [1,2,3,4]
print(lista_Inicio)
lista_Inicio += [5]
print(lista_Inicio)
lista_Inicio = lista_Inicio*3
print(lista_Inicio)