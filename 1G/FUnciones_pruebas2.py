def programa():
    dato = input("Ingrese un dato: ")
    return dato


def funcion_retorna_diccionario():
    return {'Nombres':'Richard Miguel', 'Apellidos':'Tigrero Contreras'}


recibe_funcion = programa()
print("El datos es: ", recibe_funcion)

recibe_funcion2 = funcion_retorna_diccionario()
print("El datos es: ",recibe_funcion2)

