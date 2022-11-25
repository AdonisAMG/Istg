def llenar_diccionario(valor1='', valor2='', valor3='', valor4='', valor5='', valor6=''):
    print("LLenar Dicionario")
    diccionario = {'nombres':valor1, 'apellidos': valor2, 'email': valor3, 'direccion':valor4, 'telefono': valor5, 'ciudad':valor6}
    return diccionario


def presentar_diccionario(diccionario_param={}):
    for dic in diccionario_param.values():
        print("-> ", dic)


def princiapl():
    nombres = input("Ingrese los nombres: ")
    apellidos = input("Ingrese los apellidos: ")
    email = input("Ingrese los email: ")
    direccion = input("Ingrese la direccion: ")
    telefono =  input("Ingrese el telefono: ")
    ciudad =  input("Ingrese la ciudad: ")
    vdiccionario = llenar_diccionario(nombres, apellidos, email, direccion, telefono, ciudad)
    presentar_diccionario(vdiccionario)


princiapl()