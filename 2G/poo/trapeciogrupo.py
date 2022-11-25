class FiguraGeometrica:
    def __init__ (self,lado,base,altura):
        self.lado=lado
        self.base=base
        self.altura=altura
        print("constructor FG")

    def __str__ (self):
        return f"lado: {self.lado},base: {self.base}, altura: {self.altura}"

    def perimetro(self):
        print("perimetro FG")

    def area(self):
        print("area FG")

class FiguraGeometricaTrapecio (FiguraGeometrica):
    def __init__(self,lado,base,altura,base_mayor,base_menor):
        FiguraGeometrica. __init__ (self,lado,base,altura)
        self.base_mayor=base_mayor
        self.base_menor=base_menor
        print("constr. trapecio")

    def __str__(self):
        return f"base mayor: {self.base_mayor}, base menor: {self.base_menor}, altura: {self.altura}, lado: {self.lado}"

    def perimetro(self):
        print("perimetro trapecio: ",self.base_mayor + self.base_menor + (self.lado * 2))

    def area(self):
        print("area trapecio:  ",(self.base_mayor + self.base_menor)*(self.altura)/2)


#instancia de la clase figura geometrica
f=FiguraGeometricaTrapecio(4,8,8,15,10)
print(f)
f.perimetro()
f.area()