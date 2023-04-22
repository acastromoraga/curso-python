print('*****Bienveido******')
user = 'ale'
contrasenia = 'ale123'
usuario=input('Ingresa el nombre de usuario: \n')
ingreso=input('Ingresa la contraseña: \n')
intentos = True
while(intentos):
    if(ingreso==contrasenia and user ==usuario):
        print("Bienvenido, clave válida")
        intentos = False
        break
    print("Contrseña inválida, vuelve a intentarlo")
    usuario=input('Ingresa el nombre de usuario: \n')
    ingreso=input('Ingresa la contraseña: \n')
        
