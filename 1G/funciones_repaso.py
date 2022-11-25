def funcion_basica():
    print("Hola Mundo")


def funcion_con_retorno():
    return "Hola Mundo"


def funcion_con_paramteros(dato1, dato2):
    print(dato1)
    print(dato2)


def funcion_principal():
    funcion_basica()
    vretorno = funcion_con_retorno()
    funcion_con_paramteros("Hola", "Mundo")


funcion_principal()