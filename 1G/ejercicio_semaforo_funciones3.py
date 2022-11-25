from ejercicio_semaforo_funciones2 import *


def funcion_principal():
    print("Ejercicio del Semaforo")
    dato = input("Ingrese el color del semaforo: ")
    r_funcion = evalua_semaforo(dato)
    print(r_funcion)


funcion_principal()