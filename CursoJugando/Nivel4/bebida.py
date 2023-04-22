'''
RETO PARA RESOLVER:

Haz un programa que simula una máquina de refrescos.
La máquina dispone de 4 tipos de refrescos.
Te pide el número de refresco que deseas entre el 1 y el 4.
Te informa de tu elección.
'''
print('***************Bienvenido*****************')
opción =int(input("Elige la bebida que deseas:\n(1) Coca-Cola\n(2) Fanta\n(3) Sprite\n(4) Kem\n"))
if(opción==1):
    print("Haz elegido Coca-cola")
elif(opción==2):
    print("Haz elegido Fanta")
elif(opción==3):
    print("Haz elegido Sprite")
elif(opción==4):
    print("Haz elegido Kem")
else:
    print("Haz elegido una opción incorrecta")
