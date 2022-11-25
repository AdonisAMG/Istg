def evalua_semaforo(dato):
    cadena = ""
    if dato.lower() == "amarillo":
        cadena = "No puede cruzar la calle"
    elif dato.lower() == "rojo":
        cadena = "Alto no puede cruzar la calle"
    elif dato.lower() == "verde":
        cadena = "Puede cruzar la calle"
    else:
        cadena = "Valor o informacion no valida para el semaforo"
    return cadena


def funcion_principal():
    print("Ejercicio del Semaforo")
    dato = input("Ingrese el color del semaforo: ")
    r_funcion = evalua_semaforo(dato)
    print(r_funcion)


funcion_principal()