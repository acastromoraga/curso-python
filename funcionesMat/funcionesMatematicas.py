def suma (num1,num2):
    if(num1>=0 and num2>=0):
        suma = num1+num2
    return suma

def resta (num1,num2):
    if(num1>=0 and num2>=0):
        resta = num1-num2
    return resta

def multiplicacion(num1,num2):
        if(num1>0 and num2>0):
            multi = num1*num2
        return multi
    
def division(num1,num2):
        if(num1>0 and num2>0):
            divi = num1/num2
        return divi

if __name__ == "__main__":
    print(suma(4,7))
    print(resta(4,7))
    print(multiplicacion(4,7))
    print(division(4,7))
