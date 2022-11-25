def suma(valor1=0, valor2=0):
    suma = valor1 + valor2
    print("La suma es: ", suma)


def principal():
    print("Suma 2 numeros: ")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    suma(numero1, numero2)


principal()
