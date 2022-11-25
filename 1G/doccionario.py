diccionario_datos = {"Nombres": "Adonis Alexander", "Apellidos": "Merchan Guadamud", "Edad": 18, "Nacionalidad": "Ecuatoriana"}
#                             elemento(1)                  elemento(2)               elemento(3)        elemento(4)
# forma #1
print("---------claves ---------------")
print()
for data in diccionario_datos.keys():
    print(data)

print()

print("--------- datos ----------------")
print()
for data in diccionario_datos.values():
    print(data)

print()

print("------ otra forma de presentarlos --------")
print()
# forma #2
for data in diccionario_datos:
    print(diccionario_datos[data])
