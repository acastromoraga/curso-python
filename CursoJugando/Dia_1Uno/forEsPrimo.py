numero = input("Ingresa un número: \n")
if(numero.isalpha()):
    print("Debe ingresar un Número")
elif(not numero):
    print("Debe ingresar un valor")
else:
    numero=int(numero)
    for i in range(2, numero+1):
        es_primo=True
        for x in range(2,i):
            if(i % x==0):
                es_primo=False
            
    