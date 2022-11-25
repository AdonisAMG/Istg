
def division(valor1=0, valor2=0):
    division = valor1 / valor2
    return division


def principal():
    print("Restar 2 numeros: ")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    vdivis= division(numero1, numero2)
    print("La division es: ", vdivis)


principal()