num1 = int(input("ingresa el número uno: \n"))
num2 = int(input("ingresa el número dos: \n"))
num3 = int(input("ingresa el número tres: \n"))

if(num1 > num2  and num2 > num3):
    print(f"Orden {num1} - {num2} - {num3}")
elif(num1 > num3  and num3 > num2):
    print(f"Orden {num1} - {num3} - {num2}")
elif(num2 > num1  and num1 > num3):
    print(f"Orden {num2} - {num1} - {num3}")
elif(num2 > num3  and num3 > num1):
    print(f"Orden {num2} - {num3} - {num1}")
elif(num3 > num1  and num1 > num2):
    print(f"Orden {num3} - {num1} - {num2}")
elif(num3 > num2  and num2 > num1):
    print(f"Orden {num3} - {num2} - {num1}")
else:
    print("Otro orden")