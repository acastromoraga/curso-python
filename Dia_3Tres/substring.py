#mi_variable_substring[5:12:3] desde empieza, hasta dónde sin incluir, tercer cada cuanto caracter se va a seleccionar

texto = "ABCDEFGHIJKLMN"
fragmento = texto[2] #imprme el indice 2
print(fragmento)

texto = "ABCDEFGHIJKLMN"
fragmento = texto[2:5] #desde el indice hasta el 5 no incluyendo
print(fragmento)

texto = "ABCDEFGHIJKLMN"
fragmento = texto[2:] #desde el indice 2 hasta el final
print(fragmento)

texto = "ABCDEFGHIJKLMN"
fragmento = texto[:5] #desde el indice 0 hasta el indice 5, no incluyendolo
print(fragmento)

texto = "ABCDEFGHIJKLMN"
fragmento = texto[2:10:2] #desde el indice hasta el 10 no incluyendolo, saltandose 2 caracteres el primer caracter lo imprime
print(fragmento)

texto = "ABCDEFGHIJKLMN"
fragmento = texto[::2] #desde el indice 0 hasta el final, saltandose 2 caracteres el primer caracter lo imprime
print(fragmento)

texto = "ABCDEFGHIJKLMN"
fragmento = texto[::-2] #desde el indice 0 hasta el final, saltandose 2 caracteres desde el final el primer caracter lo imprime
print(fragmento)