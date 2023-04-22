print('******Bienvenido*******')
num1 = int(input('Ingresa un número de inicio: \n'))
num2 = int(input('Ingresa un número de fin de rango: \n'))
suma =0
while(num1 <= num2):
    if(num1%3==0):
        suma = suma + num1
    num1+=1
print(f'Resultado: {suma}')