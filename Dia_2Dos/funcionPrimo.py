def numPar(numIngresado):
    es_par = False
    for i in range (1,numIngresado):
        if(i%2==0):
            es_par=True
        else:
            es_par = False
        
    return es_par

ingreso = int(input("Ingrese un número: \n"))

for x in range(1,ingreso+1):
    if numPar(x):
        print("es par el: ",x-1)
