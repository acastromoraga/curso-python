#Ejemplo 7.2.1. Crea un programa en Python que simule una bitacora. El programa debe pedirle al usuario elegir
#entre (1) Agregar un nuevo suceso, (2) Leer la bitacosa o (3) Salir. Si desea agregar un nuevo suceso, el programa
#debe ademas pedir la fecha del suceso.
elegir = True
bitacora = []
while elegir:    
    print('=====================================')
    opcion = input('Seleccione la opción que desea ejecutar:\n(1) Agregar un nuevo suceso,\n(2) Leer la bitacosa o (3)\n(4)Salir.\n')
    print('ha seleccionado la opción', opcion)
    if(opcion=='1'):
        dia = input('Ingrese día formato <dd>: \n')
        mes = input('Ingrese mes formato <mm>: \n')
        annio = input('Ingrese año: <yyyy>\n')
        texto = input('Ingrese el acontecimiento sucedido: \n')
        acontecimiento = "Fecha: " + dia + "/" + mes + "/" + annio + " Acontecimiento: " + texto
        bitacora.append(acontecimiento)
    elif(opcion=='2'):
        for i in range(len(bitacora)):    
            print(bitacora[i])
    elif(opcion=='3'):
        print('Adios!!')
        elegir = False
        break
    else:
        print('Opción no válida')