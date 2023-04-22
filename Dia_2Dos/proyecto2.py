nombre = input("Ingrese su nombre completo: ")
venta = input("ingrese su venta del mes: ")
venta = float(venta)
#comision =venta - (venta -(venta*(13/100)))
comision = venta*0.13
comision = round(comision,2)
print(f"Ok, estimado: {nombre} felicitaciones su comisión este mes es de $ {comision}")