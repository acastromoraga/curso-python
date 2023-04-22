#split(): string1.split(string2): se divide el string string1 por el separador string2. Se retorna una lista y el string
#original string1 no se ve modificado. El separador por defecto es un espacio en blanco.
frase = 'Esto es una prueba de calidad de software'
listaNueva = frase.split(' ')
print(listaNueva)

#list(string1): nos permite transformar un string string1 a una lista de caracteres.
frase = 'Esto es una prueba de calidad de software'
listaNueva2 = list(frase)
print(listaNueva2)