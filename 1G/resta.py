
def resta(valor1=0, valor2=0):
    resta = valor1 - valor2
    return resta


def principal():
    print("Restar 2 numeros: ")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    vresta= resta(numero1, numero2)
    print("La resta es: ", vresta)


principal()