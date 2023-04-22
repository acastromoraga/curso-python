import time
print("Comienza el programa.....")
tInicio = time.time()
time.sleep(5)
tFinal = time.time()
tTotal= tFinal - tInicio
print(f"fin del programa, total: {tTotal} segundos")