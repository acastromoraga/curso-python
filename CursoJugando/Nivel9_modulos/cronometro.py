import time
print("Comienza la cuenta regresiva")
tInicio = time.time()
contador = 10

while True:
    #time.sleep(1)
    time.sleep(.5)
    contador-=1
    tFinal = time.time()
    tiempoTotal = tFinal-tInicio
    print(contador)
    if contador==0:
        print(f"Fin!! tiempo total transucrrido: {tiempoTotal}")
        break