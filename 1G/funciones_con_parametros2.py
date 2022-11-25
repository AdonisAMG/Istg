def suma(valor1=0, valor2=0):
    suma = valor1 + valor2
    return suma


def principal():
    print("Suma 2 numeros: ")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    vsuma = suma(numero1, numero2)
    print("La suma es: ", vsuma)


principal()