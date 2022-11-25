from tools import Menu

class figura_geometrica_cuadrado():

    def __init__(self, lado):
        self.lado_c=lado
        self.area_c=pow(self.lado_c,2)
        self.perimetro_c=self.lado_c * 4

    def __str__(self):
        return (f"El perimetro del cuadrado es : {self.perimetro_c} y su area es: {self.area_c}")

    def calculadora_geometrica_c(self):
        print("_" * 36)
        print(f"|    lado".ljust(22,' ') + f"  {self.lado_c:.2f}    |")
        print(f"|    area".ljust(22, ' ') + f"  {self.area_c:.2f}   |")
        print(f"|    perimetro".ljust(22, ' ') + f" {self.perimetro_c:.2f}    |")

class figura_geometrica_rectangulo:

    def __init__(self, base, altura):
        self.base_re=base
        self.altura_re=altura
        self.area_re=self.base_re * self.altura_re
        self.perimetro_re=(self.base_re * 2) + (self.altura_re * 2)

    def __str__(self):
        return (f"El perimetro del rectangulo es : {self.perimetro_re} y su area es: {self.area_re}")

    def calculadora_geometrica_re(self):
        print("_" * 36)
        print(f"|    base".ljust(22,' ') + f"  {self.base_re:.2f}    |")
        print(f"|    altura".ljust(22, ' ') + f"  {self.altura_re:.2f}    |")
        print(f"|    area".ljust(22, ' ') + f"  {self.area_re:.2f}   |")
        print(f"|    perimetro".ljust(22, ' ') + f" {self.perimetro_re:.2f}    |")

class figura_geometrica_triangulo:

    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado_t_1=lado1
        self.lado_t_2=lado2
        self.lado_t_3=lado3
        self.base_t=base
        self.altura_t=altura
        self.perimetro_t=self.lado_t_1 + self.lado_t_2 + self.lado_t_3
        self.area_t= (self.base_t * self.altura_t)/2

    def __str__(self):
        return (f"El perimetro del triangulo es : {self.perimetro_t} y su area es: {self.area_t}")


    def calculadora_geometrica_t(self):
        print("_" * 36)
        print(f"|    lado 1".ljust(22,' ') + f"  {self.lado_t_1:.2f}    |")
        print(f"|    lado 2".ljust(22, ' ') + f"  {self.lado_t_2:.2f}    |")
        print(f"|    lado 3".ljust(22, ' ') + f"  {self.lado_t_3:.2f}    |")
        print(f"|    base".ljust(22, ' ') + f"  {self.base_t:.2f}    |")
        print(f"|    altura".ljust(22, ' ') + f"  {self.altura_t:.2f}    |")
        print(f"|    area".ljust(22, ' ') + f"  {self.area_t:.2f}   |")
        print(f"|    perimetro".ljust(22, ' ') + f" {self.perimetro_t:.2f}    |")


class figura_geometrica_rombo:

    def __init__(self, lado, diagonalmyr, diagonalmnr):
        self.lado_ro=lado
        self.diagonalmayor=diagonalmyr
        self.diagonalmenor=diagonalmnr
        self.area_ro=(self.diagonalmayor * self.diagonalmenor) / 2
        self.perimetro_ro=self.lado_ro * 4

    def __str__(self):
        return (f"El perimetro del rombo es : {self.perimetro_ro} y su area es: {self.area_ro}")

    def calculadora_geometrica_ro(self):
        print("_" * 36)
        print(f"|    lado".ljust(22,' ') + f"  {self.lado_ro:.2f}    |")
        print(f"|    diagonalmayor".ljust(22, ' ') + f"  {self.diagonalmayor:.2f}    |")
        print(f"|    diagonalmenor".ljust(22, ' ') + f"  {self.diagonalmenor:.2f}    |")
        print(f"|    area".ljust(22, ' ') + f"  {self.area_ro:.2f}    |")
        print(f"|    perimetro".ljust(22, ' ') + f" {self.perimetro_ro:.2f}    |")

menu_opciones_geometria={1:"MENU CUADRADO.",2:"MENU RECTANGULO.",3:"MENU TRIANGULO.",4:"MENU ROMBO.",5:"SALIR"}


menus_geometria=Menu()


lado_c=0
base_re = 0
altura_re = 0
lado_t_1 = 0
lado_t_2 = 0
lado_t_3 = 0
base_t = 0
altura_t = 0
lado_ro = 0
diagonalmayor = 0
diagonalmenor = 0


while True:

    menus_geometria.menus(menu_opciones_geometria, "Seleccione una opción")
    opc=menus_geometria.ingreso_opcion("Digite opción(1/5): ",1,5)

    if opc:
        if opc == 1:
            lado_c = float(input("Digite la medida de un lado del cuadrado : "))
            if lado_c == 0:
                menus_geometria.mensaje_pantalla("-", "Ingrese el dato por favor!!")
                continue
            calc_geo = figura_geometrica_cuadrado(lado_c)
            calc_geo.calculadora_geometrica_c()

        elif opc == 2:
            base_re = float(input("Digite la medida de la base del rectangulo : "))
            altura_re = float(input("Digite la medida de la altura del rectangulo : "))
            if base_re == 0 and altura_re == 0:
                menus_geometria.mensaje_pantalla("-", "Ingrese el dato por favor!!")
                continue
            calc_geo1 = figura_geometrica_rectangulo(base_re,altura_re)
            calc_geo1.calculadora_geometrica_re()

        elif opc == 3:
            lado_t_1 = float(input("Digite la medida del lado 1 del triangulo : "))
            lado_t_2 = float(input("Digite la medida del lado 2 del triangulo : "))
            lado_t_3 = float(input("Digite la medida del lado 3 del triangulo : "))
            base_t = float(input("Digite la medida de la base del triangulo : "))
            altura_t = float(input("Digite la medida de la altura del triangulo : "))

            if lado_t_1 == 0 and lado_t_2 == 0 and lado_t_3 == 0 and base_t == 0 and altura_t == 0:
                menus_geometria.mensaje_pantalla("-", "Ingrese el dato por favor!!")
                continue
            calc_geo3 = figura_geometrica_triangulo(lado_t_1,lado_t_2,lado_t_3,base_t,altura_t)
            calc_geo3.calculadora_geometrica_t()

        elif opc == 4:
            lado_ro = float(input("Digite la medida de un lado del rombo : "))
            diagonalmayor =  float(input("Digite la medida de la diagonal mayor del triangulo : "))
            diagonalmenor =  float(input("Digite la medida de ladiagonal menor del triangulo : "))
            if lado_ro == 0 and diagonalmayor == 0 and diagonalmenor == 0:
                menus_geometria.mensaje_pantalla("-", "Ingrese el dato por favor!!")
                continue
            calc_geo4 = figura_geometrica_rombo(lado_ro,diagonalmayor,diagonalmenor)
            calc_geo4.calculadora_geometrica_ro()

        elif opc == 5:
            menus_geometria.mensaje_pantalla("+", "Gracias por usar la calculadora geometrica. !!")
            break
    else:
        menus_geometria.mensaje_pantalla("x", "Opción Incorrecta!!")
        break