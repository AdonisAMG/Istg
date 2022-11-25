def funcion_suma():
    print("Suma de 2 numeros : ")
    dato1 = int(input("Ingrese el primer operando: "))
    dato2 = int(input("Ingrese el segundo operando: "))
    suma = dato1 + dato2
    print("La suma es : ", suma)


def funcion_resta():
    print("Resta de 2 numeros : ")
    dato1 = int(input("Ingrese el primer operando: "))
    dato2 = int(input("Ingrese el segundo operando: "))
    resta = dato1 - dato2
    print("La resta es : ", resta)


def funcion_multiplicacion():
    print("Multiplicacion de 2 numeros : ")
    dato1 = int(input("Ingrese el primer operando: "))
    dato2 = int(input("Ingrese el segundo operando: "))
    multi = dato1 * dato2
    print("La multiplicacion es : ", multi)


def funcion_division():
    print("Division de 2 numeros : ")
    dato1 = int(input("Ingrese el primer operando: "))
    dato2 = int(input("Ingrese el segundo operando: "))
    division = dato1 / dato2
    print("La division es : ", division)


def menu():
    print("Calculadora en Python con Funciones")
    print("1. Suma ")
    print("2. Resta ")
    print("3. Multiplicacion ")
    print("4. Divsion ")
    print("5. Salir ")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        funcion_suma()
    elif opcion == 2:
        funcion_resta()
    elif opcion == 3:
        funcion_multiplicacion()
    elif opcion == 4:
        funcion_division()
    else:
        exit(1)


menu()



