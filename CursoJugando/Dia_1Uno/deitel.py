
print("Hola este es\nun buen\adia\npara programar")
numero1 = input("Ingresa un número: \n")
print("id: num1" , id(numero1), type(numero1), numero1)
numero1 =int(numero1)
print("id: num1 cambio a integer" , id(numero1), type(numero1), numero1)
numero2 = input("Ingresa un segundo número: \n")
print("id: num2" , id(numero2), type(numero2), numero2)
numero2 =int(numero2)
print("id: num2 cambio a integer" , id(numero2), type(numero2), numero2)
suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
divi = numero1 / numero2
resto = numero1%numero2
print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multi)
print("La división es: ", divi)
print(f"el resto de {numero1} dividido por {numero2}  es: ", resto)