def funcion_area_cuadrado():
    print("Calculo del perimetro y  del area de un cuadrado ")
    lado_cuadrado = int(input("Ingrese el lado del cuadrado : "))
    area_cuadrado = lado_cuadrado ** 2
    perimetro_cuadrado = 4 * lado_cuadrado
    print("El perimetro del cuadrado es : ", perimetro_cuadrado, " y el area del cuadrado es : ", area_cuadrado)


funcion_area_cuadrado()
