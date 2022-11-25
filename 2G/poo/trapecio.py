#   Integrantes del grupo
# Adonis Alexander Merchan Guadamud
# Esther Gabriela Salazar Carrera
#
#

class FiguraGeometrica:
    def __init__(self,lado,base,altura):
        self.lado=lado
        self.base=base
        self.altura=altura
        print("constructor FG")

    def __str__(self):
        return f"lado: {self.lado},base: {self.base}, altura: {self.altura}"

    def perimetro(self):
        print("perimetro FG")

    def area(self):
        print("area FG")


class FiguraGeometricaTrapecio(FiguraGeometrica):
    def __init__(self, lado, base, altura, basemayor, basemenor, ladoderecho, ladoizquierdo):
        FiguraGeometrica.__init__(self, lado, base, altura)
        self.basemayor=basemayor
        self.basemenor=basemenor
        self.ladoderecho=ladoderecho
        self.ladoizquierdo=ladoizquierdo
        print("constructor trapecio")

    def __str__(self):
        return f"base mayor: {self.basemayor}, base menor: {self.basemenor}, altura: {self.altura}, lado derecho: {self.ladoderecho}, lado izquierdo : {self.ladoizquierdo}"

    def perimetro(self):
        print("El perimetro del trapecio es: ",self.basemayor + self.basemenor + self.ladoderecho + self.ladoizquierdo)

    def area(self):
        print("El area del trapecio es:  ",(((self.basemayor + self.basemenor) * (self.altura))/2))


#instancia de la clase figura geometrica
f=FiguraGeometrica(10,7,5)
print(f)
f.perimetro()
f.area()

print()
print()

print("TRAPECIO")

print()
#instancia de la clase figura geometrica trapecio
# (lado,base,altura,basemayor,basemenor,ladoderecho,ladoizquierdo)
t=FiguraGeometricaTrapecio(10,7,5,9,7,4,4)
print()
print(t)
print()
t.perimetro()
print()
t.area()