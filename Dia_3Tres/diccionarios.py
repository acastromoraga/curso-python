diccionario = {'c1': 'valor1','c2': 'valor2' }
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Juan', 'apellido': 'Soto', 'peso':88, 'talla': 45.7}
consulta = (cliente['peso'])
print(consulta)


######
diccio = {'c1':55, 'c2':['ana','fuentes',45], 'c3':{'s1':'fuerza', 's2':'gravedad'}}
consultadiccionario = (diccio['c2'][1])
print(consultadiccionario)
consultadiccionario2 = (diccio['c3']['s2'])
print(consultadiccionario2)

#######
diccio2 = {'c1':['a','b','c'],'c2':['d','e','f']}
consulta3 = (diccio2['c2'][1]).upper()
print(consulta3)

##agregar contenido al diccionario
diccio2['c3']= 'beta'
print(diccio2)

##sobreescribir un diccionario
diccio2['c3'] = 'cambio de valor'
print(diccio2)
print(diccio2.keys())
print(diccio2.values())
print(diccio2.items())

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia'
print(mi_dic)