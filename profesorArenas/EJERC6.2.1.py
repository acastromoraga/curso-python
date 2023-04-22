texto = input("Ingrese una cadena de texto: \n")
texto = texto.lower()
if(texto.isalpha()):
    while True:
        conversion = ""
        mayusculas =input("Desea pasar a mayúsulas: \nSeleccione 1 = si\nSeleccione 2 = no\n")
        seleccion=int(mayusculas)
        if(seleccion==1):
           print(texto.upper())
        else:
            print("Adios!")
            break
            
        texto = input("Ingrese una cadena de texto: \n")
