#crear un ejercicio en python que me permita ingresar los datos para el calculo de area y perimetro de las siguienes figuras
# cuadrado rectangulo triangualo y circulo, los datos de entrada para generar lo calculo deben ser mayores que cero



while True:

    print("Area y perimetro del cuadrado ")
    lado = int(input("Ingrese la medida del lado : "))

    if lado > 0:
        area = lado * lado
        perimetro = lado * 4
        print("El area del cuadrado es : ", area, " y el perimetro es  : ", perimetro)
    else:
        print("Los datos ingresados no son validos para el proceso")

    print()


    print("Area y perimetro del rectangulo ")
    base = int(input("Ingrese la medida de la base : "))
    altura = int(input("Ingrese la medida de la altura : "))
    if base > 0 and altura > 0:
        area = base * altura
        perimetro = 2 * altura + 2 * base
        print("El area del rectangulo es : ", area, " y el perimetro es  : ", perimetro)
    else:
        print("Los datos ingresados no son validos para el proceso")


    print()


    print("Area y perimetro del triangulo ")
    lado1 = int(input("Ingrese la medida del lado1 : "))
    lado2 = int(input("Ingrese la medida del lado2 : "))
    lado3 = int(input("Ingrese la medida del lado3 : "))
    base = int(input("Ingrese la medida de la base : "))
    altura = int(input("Ingrese la medida de la altura : "))
    if lado1 > 0 and lado2 > 0 and lado3 > 0 and base > 0 and altura > 0:
        area = lado1 + lado2 + lado3
        perimetro = (base * altura) / 2
        print("El area del rectangulo es : ", area, " y el perimetro es  : ", perimetro)
    else:
        print("Los datos ingresados no son validos para el proceso")


    print()


    print("Area y perimetro del circulo ")

    radio = int(input("Ingrese la medida del radio : "))
    pi = 3.1416

    if radio > 0:
        area = pi * (radio ** 2)
        perimetro = 2 * pi * radio
        print("El area del circulo es : ", area, " y el perimetro del circulo es  : ", perimetro)
    else:
        print("Los datos ingresados no son validos para el proceso")


        options = input("desea continuar S/N: ")
        if options.lower() == "s":
            continue
        elif options.lower() == "n":
            break
        else:
            print("dato no valido")
            break