diccionario = {'datoclave':'Informacion', 'nombres':'Richard Miguel'}
#               key            data     ,   key       dat
print(diccionario)
print(diccionario['datoclave'])
print(diccionario['nombres'])
print(diccionario.get('nombres'))
informacion_por_teclado = input("Ingrese informacion para diccionario: ")
diccionario2 = {'dato_teclado': informacion_por_teclado}
print(diccionario)
print(diccionario2)




# forma #1
print("---------claves ---------------")


for data in diccionario_datos.keys():
print(data)

print()

print("--------- datos ----------------")

for data in diccionario_datos.values():
print(data)

print()

print("------ otra forma de presentarlos --------")

# forma #2
for data in diccionario_datos:
    print(diccionario_datos[data])