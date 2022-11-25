def funcion_suma():
    print("Suma 2 numeros: ")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    suma = numero1 + numero2
    return suma


def funcion_resta():
    print("Resta 2 numeros : ")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    resta = numero1 - numero2
    return resta

def funcion_multiplicacion():
    print("Multiplicacion 2 numeros : ")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    multiplicacion = numero1 * numero2
    return multiplicacion


def funcion_division():
    print("Diivision 2 numeros")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    division = numero1 / numero2
    return division


def principal():
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


principal()