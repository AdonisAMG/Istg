def llenar_lista(valor1):
    print("LLenar Lista")
    contador = 0
    lista = []
    while contador < valor1:
        dato = input("Ingrese dato a la lista: ")
        lista.append(dato)
        contador= contador+1
    return lista


def presentar_lista(lista=[]):
    for lis in lista :
        print("item --> ", lis)


def principal():
    print("Item de Productos")
    cantidad_datos = int(input("Ingrese la Cantidad de Articulos: "))
    vlista = llenar_lista(cantidad_datos)
    presentar_lista(vlista)


principal()