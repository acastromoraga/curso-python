num = int(input("Ingresa un número: \n"))
if(num>0):
    if(num%3==0):
        print("Multiplo de 3")
    elif(num%5==0):
        print("Multiplo de 5")
    else:
        print("No es multiplo ni de 3 ni de 5")
else:
    print("Número inválido")   