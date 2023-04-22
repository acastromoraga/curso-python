ninos = int(input('Ingresa la cantidad de niños: \n'))
if(ninos > 0):
    caramelos = int(input('Ingresa la cantidad de caramelos: \n'))
    if(caramelos > 0):
        divisionSinResto = caramelos // ninos
        restoCaramelos = caramelos%ninos
    else:
        print('Niños debe ser mayor a cero')
else:
    print('Niños debe ser mayor a cero')

print(f"Repartir {caramelos} caramelos entre {ninos} niños")
print(f"A cada niño le tocan {divisionSinResto} caramelos")
print(f"Sobran {restoCaramelos} caramelos")