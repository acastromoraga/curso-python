#hacer un programa donde se de la opción de 
#(1) Ingresar un el listado de personas: fecha(dd-mm-yyyy), nombre, apellido, edad, pais
#(2) Leer el listado ordenado por nombre
#(3) Leer por orden de apellido
#(4) Leer por orden de edad
#(5) Leer por orden de fecha
#(6) Salir del programa
filas = 0
personas = [filas][5]
eleccion = True
while eleccion:
    print('=======Bienvenido==========')
    eleccion = input('Ingrese la opción que desea realizar:\n(1) Ingresar un el listado de personas: fecha(dd-mm-yyyy), nombre, apellido, edad, pais\n(2) Leer el listado ordenado por nombre\n(3) Leer por orden de apellido\n(4) Leer por orden de edad\n(5) Leer por orden de fecha\n(6) Salir del programa\n')
    if(eleccion==1):
        dia = input('Ingrese el dia inscripción con formato <dd>: \n')
        mes = input('Ingrese el dia inscripción con formato <mm>: \n')
        annio = input('Ingrese el dia inscripción con formato <yyyy>: \n')
        fecha = dia+"/"+mes+"/"+annio
        fechaNum = int(annio+mes+dia)
        nombre = input('Ingrese nombre: \n')
        apellido = input('Ingrese apellido: \n')
        edad = int(input('Ingrese apellido: \n'))
        pais = input('Ingrese apellido: \n')
    #elif(eleccion==2):
    #elif(eleccion==3):
    #elif(eleccion==4):
    #elif(eleccion==5):
    #elif(eleccion==6):
    else:
        print('Opción inválida')