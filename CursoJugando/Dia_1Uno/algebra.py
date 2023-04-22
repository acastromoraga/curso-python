numero1 = input("Ingresa un primer número: \n")
if (numero1.isalpha()):
    print(f"Error, lo ingresado no es un número")
elif not numero1:
    print(f"Error, No ha ingresado un número")
else:
    numero1 = int(numero1)
    numero2 = input("Ingresa un segundo número: \n")
    if (numero2.isalpha()):
        print(f"Error, lo ingresado no es un número")
    elif not numero2:
        print(f"Error, No ha ingresado un número")
    else:
        numero2 = int(numero2)
        numero3 = input("Ingresa un tercero número: \n")
        if (numero3.isalpha()):
            print(f"Error, lo ingresado no es un número")
        elif not numero3:
            print(f"Error, No ha ingresado un número")
        else:
            numero3 = int(numero3)
            print("Calculando!!!")
            if (numero1 == 0):
                print(f"La función no es cuadrática, ya que a = {numero1}")
            elif((numero2**2-4*numero1*numero3)>= 0):
                print("Tiene dos soluciones reales")
            elif((numero2**2-4*numero1*numero3)==0):
                print("Tiene una solución reales")
            elif((numero2**2-4*numero1*numero3)<= 0):
                print("No tiene una solución reales")