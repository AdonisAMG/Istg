diccionario_dinamico = {}
while True:
    print("Llenar Diccionario Dinamicamente ")
    clave = input("Ingrese la clave o etiqueta para el dato: ")
    dato = input ("Ingrese el dato: ")
    diccionario_dinamico[clave] = dato

    opcion = input("Desea continuar s/n ")

    if(opcion.lower()=='n'):
        break
print(diccionario_dinamico)
print("--------------------- Informacion de diccionario ----------------------")
for data in diccionario_dinamico.values():
    print(data)