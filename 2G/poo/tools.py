class Menu:
    def mensaje_pantalla(self, caracter,mensaje="", valor=""):
        print(caracter * 150)
        mensaje += valor
        print(f"{mensaje.center(150, ' ')}")
        print(caracter * 150)

    def menus(self,caracter,menu_opciones,cabecera):
        self.mensaje_pantalla(caracter,cabecera)
        for opcion, texto in menu_opciones.items():
            print(f"{str(opcion).rjust(65, ' ')}.-  {texto}")

    def ingreso_opcion(self,msg,minimo,maximo):
        #opcion = int(input("Digite su opcion: "))
        opcion = int(input(msg))
        if opcion in range(minimo,maximo+1):
            return opcion
        return False

    def validar_letras(self,lista_letras,msg1,msg2):
        valor=""
        while True:
            valor = input(msg1).upper()
            #if tipo_cuenta in ("A", "C"):
            if valor in lista_letras:
                break
            else:
                print(msg2)
        return valor