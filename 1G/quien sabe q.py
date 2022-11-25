def llenar_diccionario(valor1='', valor2='', valor3=''):
    print("LLenar Dicionario")
    diccionario = {'direccion':valor1, 'telefono': valor2, 'ciudad': valor3}
    print("El diccionario es: ", diccionario)


def princiapl():
    direccion = input("Ingrese su direccion: ")
    telefono = input("Ingrese su # d telefono: ")
    ciudad = input("Ingrese el nombre de su ciudad: ")
    llenar_diccionario(direccion, telefono, ciudad)


princiapl()
