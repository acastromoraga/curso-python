contrasena1 = input("Ingresa una contraseña: \n")
if(not contrasena1):
    print("Ingresa una contrasena correcta: \n")
else:
    contrasena2 = input("Ingresa contraseña nuevamente: \n")
    if(not contrasena2):
        print("Ingresa una contrasena correcta: \n")
    elif(contrasena2!=contrasena1):
        contrasena2 = input("Ingresa contraseña correcta nuevamente: \n")
        if(contrasena1==contrasena2):
            contrasena3 = input("Ingresa contraseña nuevamente: \n")
            if(contrasena3==contrasena2==contrasena1):
                print("correcto")
        else:
            print("contraseña incorrecta")

    elif(contrasena1==contrasena2):
        contrasena3 = input("Ingresa contraseña nuevamente: \n")
        if(contrasena3==contrasena2==contrasena1):
            print("correcto")
        else:
            print("contraseña incorrecta")
    else:
        contrasena3 = input("La contraseña debe ser la misma,Ingresa contraseña nuevamente: \n")
        if(contrasena3==contrasena2==contrasena1):
            print("correcto")
        else:
            print("contraseña incorrecta")
