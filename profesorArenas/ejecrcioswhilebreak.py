while True :
    a = float ( input ('Ingrese el primer n´u mero a: '))
    b = float ( input ('Ingrese el segundo n´u mero b: '))
    menu = 'Ingrese la operaci ´on: \n 1) Suma \n 2) Resta \n 3) Mult \n 4) Div \n 5) Salir \n'
    opcion = input ( menu )
    if opcion == '1':
        suma = a + b
        print ('La suma es: ' + str( suma ))
    elif opcion == '2':
        resta = a - b
        print ('La resta es: ' + str ( resta ))
    elif opcion == '3':
        mult = a * b
        print ('La multiplicaci ´on es: ' + str( mult ))
    elif opcion == '4':
        div = a / b
        print ('La divisi ´on es: ' + str ( div ))
    elif opcion == '5':
        print ('Adi ´os!')
        break
    else :
        print ('La operaci ´on ingresada no es v´a lida ')