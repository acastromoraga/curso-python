texto = "Este es el texto de federico"
resultado = texto
print(resultado)

#Transformar los caracteres en mayúsculas
resultado= texto.upper()
print(resultado)

#Transformar los caracteres en minusculas de indice 2
resultado = texto[3].upper()
print(resultado)
mayusculas = resultado.islower()
print(mayusculas)

#Separar por los espacios vacios en elementos independientes y guardar dentro de una lista
resultado=texto.split()
print(resultado)

#Separar por un caracter partícular en elementos independientes y guardar dentro de una lista
resultado=texto.split("x")
print(resultado)

#unir cadenas de texto
texto1 = "Aprender"
texto2 = "Python"
texto3 = "es"
texto4 = "genial"
#unir los textos mediante un separador
union = " ".join([texto1,texto2,texto3,texto4])
print(union)

#busca un determinado caracter dentro de un string, se diferencia con el metodo index(), ya que da resultado -1 si no op encuentra
resultado = union.find("y")
print(resultado)

#Reemplazar un pedazo del texto y reemplazarlo por otro
texto = "Este es el texto de federico"
resultado = texto.replace("texto", "matemática")