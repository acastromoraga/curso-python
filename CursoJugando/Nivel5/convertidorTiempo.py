segundos = int(input('Ingrese los segundos'))
if(segundos>=0):
    minutos= segundos//60
    restoSegundos = segundos%60
    horas = minutos//60
    restominutos = minutos%60 
else:
    print('Debe ingresar un número positivo de segundos')
print(f'El total de {segundos} ingresados son: {horas} horas con {restominutos} y {restoSegundos} segundos')