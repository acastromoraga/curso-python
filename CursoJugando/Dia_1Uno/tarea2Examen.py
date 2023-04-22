prueba1 = input('Ingresa la nota de la prueba 1: \n')
prueba1 = float(prueba1)
prueba2 = input('Ingresa la nota de la prueba 2: \n')
prueba2 = float(prueba2)
prueba3 = input('Ingresa la nota de la prueba 3: \n')
prueba3 = float(prueba3)
examen = input('Ingresa la nota del examen: \n')
examen = (float(examen))*0.4
promedio = round(((prueba1+prueba2+prueba3)/3),2)
ponderacion = promedio*0.6
notaFinal = ponderacion + examen
print(f"Promedio de notas: {promedio}")
print(f"Nota final: {notaFinal}")
if notaFinal>=4:
    print("Usted ha aprobado")
else:
    print("Usted ha reprobado")