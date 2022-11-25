# De la siguiente lista e elementos se debe realizar la busqueda de elementos que se ingresen por pantalla y que nos
# indique cuantas veces se repite el elemnto


def busqueda_dato(lista=[]):
    dato_entrada = input("Ingrese el valor o dato a buscar: ")
    cantidad = lista.count(dato_entrada)
    return cantidad

def funcion_principal():
    lista = ['Ecuador', 'Colombia', 'Peru', 'Uruguay', 'Chile', 'Brasil', 'Ecuador', 'Peru', 'Chile', 'Ecuador']
    nveces = busqueda_dato(lista)
    print("El dato se encuentra ", nveces, " veces")


funcion_principal()