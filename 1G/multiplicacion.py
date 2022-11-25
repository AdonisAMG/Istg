
def multiplicacion(valor1=0, valor2=0):
    multiplicacion = valor1 * valor2
    print("La multiplicacion es: ", multiplicacion)


def principal():
    print("multiplicar 2 numeros: ")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    multiplicacion(numero1, numero2)


principal()