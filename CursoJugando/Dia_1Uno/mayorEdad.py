edad = input("Ingrese su edad: \n")
if (edad.isalpha()):
    print("Error!!!, usted ha ingresado una letra!!")
elif not edad:
    print("Error!!!, usted no ha ingresado edad")

else:
    edad = int(edad)
    if(edad>0 and edad <18):
        print("Usted es menor de edad")
    elif (edad >= 18):
         print("Usted es mayor de edad")
    elif(edad == 0):
        print("Usted ingresó un 0")
    else:
        print("Usted ingresó un caracter extraño")