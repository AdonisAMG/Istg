#       Integrantes del grupo:
# Adonis Alexander Merchan Guadamud
# Esther Gabriela Salazar Carrera
# Giovanni Israel Salinas Guzman
# Dayanara Gabriela Silva Perez
# Pedro Wilfrido Vargas Adriano


from tools import Menu
from random import randrange

#deber sección 1
class cliente:
    def crear_cliente(self, nombres, cedula, correo, direccion, nacionalidad, numero_telefono, contacto, fecha_nacimiento):
        self.nombres = nombres
        self.cedula = cedula
        self.correo = correo
        self.direccion = direccion
        self.nacionalidad = nacionalidad
        self.numero_telefono = numero_telefono
        self.contacto = contacto
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        presentar = f""" Nombres : {self.nombres}\n Cédula : {self.cedula}\n Correo : {self.correo}\n Dirección : {direccion}\n Nacionalidad : {self.nacionalidad}\n Número de teléfono : {self.numero_telefono}\n Numero a contactar en caso de emergencia : {self.contacto}\n Fecha de nacimiento : {self.fecha_nacimiento}"""
        return presentar


class CuentaBancaria:

    #método que permite crear una cuenta por primera vez
    def crear_cuenta(self,numero_cuenta,tipo_cuenta,saldo,clave):
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo

        #tipo cuenta
        # A ahorro / C Corriente
        self.tipo_cuenta=tipo_cuenta
        self.clave=clave

        #atributo que define si una cuenta se encuentra activa o inactiva
        # true   cuenta   activa
        # False  cuenta   inactiva
        self.estado=True

    #método que permite generar un número de cuenta, comenzando por la secuencia 0900....
    def generar_numero_cuenta(self):
        global secuencia_cuenta
        secuencia_cuenta += 1

        sec_txt = str(secuencia_cuenta)
        if len(sec_txt) == 2:
            sec_txt = "00" + str(secuencia_cuenta)
        elif len(sec_txt) == 3:
            sec_txt = "0" + str(secuencia_cuenta)
        return sec_txt


    #método especial String para poder imprimir nuestro objeto en el momento que utilizamos la instrucción print()
    def __str__(self):
        presentar=f"numero_cuenta: {self.numero_cuenta}, tipo_cuenta: {self.tipo_cuenta}, saldo: {self.saldo}, clave: {clave}"
        return presentar

    #método buscar cuenta permite buscar una cuenta en nuestra lista de cuentas
    #recibe:
    #  lista: es una lista de objetos de tipo CuentaBancaria
    #  cuenta es el numero de cuenta a buscar en la lista
    #devuelve:
    #  si encuentra el # de cuenta: la posición en la lista de cuentas
    #  si no encuentra el # de cuenta: devuelve -1
    def buscar_cuenta(self, lista, cuenta):
        pos = 0
        for i in lista:
            if i.numero_cuenta == cuenta:
                return pos
            pos += 1
        return -1


    #método que permite modificar una cuenta bancaria, recibe:
    #  lista: es una lista de objetos de tipo CuentaBancaria
    #  posición  es la índice del  número de cuenta en nuestra lista de objetos tipo CuentaBancaria
    #  tipo_cuenta,saldo son los valores  con los cuales se modificarán los atributos tipo_cuenta y saldo respectivamente
    def modificar_cuenta(self,lista,posicion,tipo_cuenta,saldo):
        lista[posicion].tipo_cuenta=tipo_cuenta
        lista[posicion].saldo=saldo
        lista[posicion].clave=randrange(1000,9000)


    #método que permite eliminar una cuenta bancaria, recibe:
    #La eliminación es lógica, cambia de estado el atributo estado de True a Falso
    #  lista: es una lista de objetos de tipo CuentaBancaria
    #  posición  es la índice del  número de cuenta en nuestra lista de objetos tipo CuentaBancaria
    def eliminar_cuenta(self,lista,posicion):
        lista[posicion].estado=False


    #método para listar todas las cuentas bancarias
    #recibe:
    #  lista: es una lista de objetos de tipo CuentaBancaria
    def listar_cuentas(self,lista):
        print("# DE CUENTA      TIPO DE CUENTA       SALDO      CLAVE      ESTADO")
        for i in lista:
            # "CORRIENTE"
            # "AHORRO   "
            tcuenta = "AHORRO   " if i.tipo_cuenta == "A" else "CORRIENTE"

            # 0901  AHORRO     12.0     ****  ACTIVO
            # 0902  CORRIENTE  3000.98  ****  ACTIVO
            saldo=str(i.saldo).ljust(10,' ')
            clave = str(i.clave).replace(str(i.clave),"****")
            estado = "ACTIVO" if i.estado == True else "INACTIVO"

            # clave = str(i.clave)
            # print(type(clave))
            # #"8942"   "****"
            # clave.replace(clave,"****")
            print(f"{i.numero_cuenta}               {tcuenta}          {saldo} {clave}       {estado}")

    # suma a nuestro saldo actual
    def depositar(self):
        pass

    # resta a nuestro saldo actual
    def retirar(self):
        pass

    #resta a nuestro saldo actual
    def transferir(self):
        pass

    #presentacion del saldo
    def estado_cuenta(self):
        pass
cb = CuentaBancaria()
secuencia_cuenta=900
menu_opciones_administrativo={1:"Crear Cuenta",2:"Modificar Cuenta",3:"Eliminar Cuenta",4:"Listar Cuentas",5:"ingresar clientes" ,   6:"Salir"}
menu_opciones=Menu()
lista=[]

# [0]  0901,C,1000,****
# [1]  0902,C,1000,****
# [2]  0903,C,1000,****

while True:
    menu_opciones.menus("-", menu_opciones_administrativo, "Menu de Cuentas Bancarias")
    opc=menu_opciones.ingreso_opcion("Digite su opcion: ",1,6)
    if opc:
        if opc == 1:
            menu_opciones.mensaje_pantalla("-","Creacion de cuentas")
            numero_cuenta=cb.generar_numero_cuenta()
            print("Numero de cuenta generada: ",numero_cuenta)
            while True:
                tipo_cuenta=input("Tipo de Cuenta: A - Ahorro / C - Corriente: ").upper()
                if tipo_cuenta in ("A","C"):
                    break
                else:
                    menu_opciones.mensaje_pantalla("*","Por favor digite A para Ahorro ó C para Corrienre!!")

            saldo= float(input("Digite Saldo inicial: "))
            clave=randrange(1000,9000)
            cb.crear_cuenta(numero_cuenta,tipo_cuenta,saldo,clave)
            lista.append(cb)
            menu_opciones.mensaje_pantalla("+", "La cuenta ah sido creada de forma exitosa")

        elif opc == 2:
            menu_opciones.mensaje_pantalla("-","Modificacion de Cuentas")
            cuenta = input("Digite el numero de cuenta a modificar: ")
            posicion = cb.buscar_cuenta(lista,cuenta)
            if posicion==-1:
                menu_opciones.mensaje_pantalla("*","No existe ese numero de cuenta")
                continue
            else:
                while True:
                    tipo_cuenta = input("Tipo de Cuenta: A - Ahorro / C - Corriente: ").upper()
                    if tipo_cuenta in ("A", "C"):
                        break
                    else:
                        menu_opciones.mensaje_pantalla("*", "Por favor digite A para Ahorro ó C para Corrienre!!")
                saldo = float(input("Digite Saldo inicial: "))
                cb.modificar_cuenta(lista,posicion,tipo_cuenta,saldo)

        elif opc == 3:
            menu_opciones.mensaje_pantalla("-","Eliminacion de Cuentas")
            cuenta = input("Digite el numero de cuenta a eliminar: ")
            posicion = cb.buscar_cuenta(lista, cuenta)
            if posicion == -1:
                menu_opciones.mensaje_pantalla("*", "No existe ese número de cuenta")
                continue
            else:
                cb.eliminar_cuenta(lista,posicion)
                menu_opciones.mensaje_pantalla("+", "cuenta modificada con éxito")

        elif opc == 4:
            menu_opciones.mensaje_pantalla("-","Listar Cuentas")
            cb = CuentaBancaria()
            #print(cb)
            cb.listar_cuentas(lista)

        #opcion 5 creacion de clientes
        elif opc == 5:
            #deber sección 2

            menu_opciones.mensaje_pantalla("-", "Crear clientes")
            nombres = input("¿Cuáles son sus nombre: ")
            cedula = input("¿Cuál es su número de cedula: ")
            correo = input("¿Cuál es su correo electrónico: ")
            direccion = input("¿Cuál es su dirección: ")
            nacionalidad = input("¿Cuál es su nacionalidad: ")
            numero_telefono = input("¿Cuál es su número de telefono: ")
            contacto = input("¿Cuál es el número a llamar en caso de emergencia: ")
            fecha_nacimiento = input("¿Cuál es su fecha de nacimiento: ")

            menu_opciones.mensaje_pantalla("-", "¡¡¡Cliente creado con exito!!!")

            clientes = cliente()
            clientes.crear_cliente(nombres, cedula, correo, direccion, nacionalidad, numero_telefono, contacto, fecha_nacimiento)
            print(clientes)


        #salir del menu
        else:
            menu_opciones.mensaje_pantalla("+","Gracias por usar la aplicación")
            break
    else:
        menu_opciones.mensaje_pantalla("*","Opción Incorrecta")