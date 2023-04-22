numero1 = input("Ingrese un número: \n")
numero2 = input("Ingrese un segundo número: \n")
numero1=int(numero1)
numero2=int(numero2)
oparacion = input("Seleccione la operación que desea: \nSumar: 1\nRestar: 2\nMultiplicar: 3\nDividir: 4\nSalir: 5\n")
opcion = input(oparacion)
if(opcion=='1'):
    suma = int(numero1) + int(numero2)
    print("suma:",suma)
elif(opcion=='2'):
    resta = int(numero1) - int(numero2)
    print("resta:",resta)
elif(opcion=='3'):
    multi = int(numero1) * int(numero2)
    print("multiplicación:",multi)
elif(opcion=='4'):
    divi = int(numero1) / int(numero2)
    print("división:",divi)
elif(opcion=='5'):
        print("salir")
else:
    print("OPCION INVÁLIDA, ADIOS")
                