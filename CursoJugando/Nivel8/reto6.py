'''
Tenemos una tupla con los meses de laño. Queremos saber qué memeses tienen en su nombre la letra "b"
'''
meses_con_b_tupla = ()
meses_con_b_lista = []
meses = ['Enero', 'Febrero','Marzo','Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre ','Noviembre', 'Diciembre']

for mes in meses:
        if 'b' in mes:
            #print(mes)
            meses_con_b_tupla = meses_con_b_tupla + (mes,)
            meses_con_b_lista = meses_con_b_lista + [mes]
print(f"Tuple: {meses_con_b_tupla}")
print(f"Lista: {meses_con_b_lista}")


