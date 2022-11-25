from funciones_matematicas import *


def principal():
    while True:
        print("Menu de Operaciones Matematicas ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicaciom")
        print("4. Division")
        print("5. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            vsuma = funcion_suma()
            print("La suma es : ", vsuma)
        elif opcion == "2":
            vresta = funcion_resta()
            print("La resta es : ", vresta)
        elif opcion == "3":
            vmulti = funcion_multiplicacion()
            print("La multiplicacion es : ", vmulti)
        elif opcion == "4":
            vdiv = funcion_division()
            print("La division es : ", vdiv)
        else:
            exit(1)
        opcion_c = input("Desea continuar S/N : ")
        if opcion_c.lower() == "n":
            break


principal()