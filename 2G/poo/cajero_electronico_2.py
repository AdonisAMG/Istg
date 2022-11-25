from  tools import Menu
from random import randrange

#deber sección 1
class Cliente:

    def crear_cliente(self,nombres,
                            nacionalidad,
                            direccion,
                            cedula,
                            correo,
                            fecha_nacimiento,
                            tlf_conv,
                            tlf_movil,
                            tlf_contacto,
                            contacto):

        self.nombres= nombres
        self.nacionalidad=nacionalidad
        self.direccion=direccion
        self.cedula=cedula
        self.correo=correo
        self.fecha_nacimiento=fecha_nacimiento
        self.tlf_conv= tlf_conv
        self.tlf_movil=tlf_movil
        self.tlf_contacto= tlf_contacto
        self.contacto=contacto



# nombres
# nacionalidad
# direccion
# cedula
# correo
# fecha  de  nacimiento
# numero  de   telefono   conv
# numero  de   telefono   movil
# numero  de   telefono  contacto
# contacto(nombre)





class CuentaBancaria:
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

    def generar_numero_cuenta(self):
        global secuencia_cuenta
        secuencia_cuenta += 1

        sec_txt = str(secuencia_cuenta)
        if len(sec_txt) == 2:
            sec_txt = "00" + str(secuencia_cuenta)
        elif len(sec_txt) == 3:
            sec_txt = "0" + str(secuencia_cuenta)
        return sec_txt

    def __str__(self):
        presentar=f"numero_cuenta: {self.numero_cuenta}, tipo_cuenta: {self.tipo_cuenta}, saldo: {self.saldo}, clave: {clave}"
        return presentar

    def modificar_cuenta(self,lista,posicion,tipo_cuenta,saldo):
        lista[posicion].tipo_cuenta=tipo_cuenta
        lista[posicion].saldo=saldo
        lista[posicion].clave=randrange(1000,9000)

    def elimina_cuenta(self,lista,posicion):
        lista[posicion].estado=False


    def buscar_cuenta(self,lista,cuenta):
        pos=0
        for i in lista:
            if i.numero_cuenta == cuenta:
                return pos
            pos+=1
        return -1


    #método para listar todas las cuentas
    def listar_cuentas(self,lista):
        print("# DE CUENTA    TIPO DE CUENTA      SALDO     CLAVE     ESTADO")
        for i in lista:
            tcuenta="AHORRO" if i.tipo_cuenta=="A" else "CORRIENTE"
            clave = str(i.clave).replace(str(i.clave),"****")
            estado = "ACTIVO" if i.estado == True else "INACTIVO"
            # clave = str(i.clave)
            # print(type(clave))
            # #"8942"   "****"
            # clave.replace(clave,"****")
            print(f"{i.numero_cuenta}               {tcuenta}           {i.saldo}           {clave}       {estado}")

    # suma a nuestro saldo actual
    def depositar(self,lista,posicion,valor,concepto):
        lista[posicion].saldo+=valor
        # lista[posicion].saldo=lista[posicion].saldo+valor

        # cuenta 0901
        # 03/02/2022  dep 100, 230.00
        # 03/02/2022  ret  10, 220.00
        # saldo disp  220.


    # resta a nuestro saldo actual
    def retirar(self,lista,posicion,valor,concepto):
        lista[posicion].saldo-=valor

    #resta a nuestro saldo actual
    def transferir(self,lista,posicion,valor,concepto):
        lista[posicion].saldo-=valor

    #presentacion del saldo
    def estado_cuenta(self):
        pass

cb = CuentaBancaria()
secuencia_cuenta=900
menu_opciones_administrativo={1:"Crear Cuenta",2:"Modificar Cuenta",3:"Eliminar Cuenta",4:"Listar Cuentas",5:"menu clientes" , 6:"Depositar",7:"retirar",8:"transferencia",  9:"Salir"}
menu_opciones_cliente={1:"Crear cliente",2:"modificar cliente",3:"Eliminar cliente",4:"regresar"}
menu_opciones=Menu()
lista=[]
lista_clientes=[]

# [0]  0901,C,1000,****
# [1]  0902,C,1000,****
# [2]  0903,C,1000,****


def menu_clientes():
    while True:
        menu_opciones.menus("-",menu_opciones_cliente,"Menu clientes")
        opc=menu_opciones.ingreso_opcion("Digite opcion: 1/4: ",1,4)
        if opc:
            if opc==1:
                menu_opciones.mensaje_pantalla("-","Crear cliente")

                nombres=input("nombres: ")
                nacionalidad=input("nacionalidad: ")
                direccion=input("direccion: ")
                cedula=input("cedula: ")
                correo=input("correo: ")
                fecha_nacimiento=input("fecha_nacimiento: ")
                tlf_conv=input("tlf_conv: ")
                tlf_movil=input("tlf_movil: ")
                tlf_contacto=input("tlf_contacto: ")
                contacto=input("contacto: ")
                clientes = Cliente()
                clientes.crear_cliente(nombres,
                            nacionalidad,
                            direccion,
                            cedula,
                            correo,
                            fecha_nacimiento,
                            tlf_conv,
                            tlf_movil,
                            tlf_contacto,
                            contacto)
                lista_clientes.append(clientes)
                menu_opciones.mensaje_pantalla("-", "Cliente creado con exito")

                # [0],juan,xxx,0912
                # [1],david,xxx,0916
                # [2],abel,xxx,09145

            elif opc==2:
                menu_opciones.mensaje_pantalla("-","modificar cliente")
            elif opc == 3:
                menu_opciones.mensaje_pantalla("-", "eliminar cliente")
            else:
                menu_opciones.mensaje_pantalla("-","regresar")
                break
        else:
            menu_opciones.mensaje_pantalla("*","Opcion incorrecta")



while True:
    menu_opciones.menus("-", menu_opciones_administrativo, "Menu de Cuentas Bancarias")
    opc=menu_opciones.ingreso_opcion("Digite su opcion: ",1,8)
    if opc:
        if opc == 1:
            menu_opciones.mensaje_pantalla("-","Creacion de cuentas")
            cb = CuentaBancaria()
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
            if posicion == -1:
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
                cb.elimina_cuenta(lista,posicion)
                menu_opciones.mensaje_pantalla("+", "cuenta modificada con éxito")

        elif opc == 4:
            #menu_opciones.mensaje_pantalla("-","Listar Cuentas")
            #print(cb)
            cb.listar_cuentas(lista)

        #opcion 5 creacion de clientes
        elif opc == 5:
            #menu_opciones.mensaje_pantalla("-", "Creación de clientes")
            #deber sección 2
            menu_clientes()

        elif opc== 6:
            menu_opciones.mensaje_pantalla("-", "Deposito de cuentas")
            cuenta=input("digite numero de cuenta para realizar deposito: ")
            pos = cb.buscar_cuenta(lista,cuenta)
            if pos==-1:
                menu_opciones.mensaje_pantalla("*","Cuenta no existe")
                continue
            valor=float(input("Digite el valor del deposito: "))
            cb.depositar(lista,pos,valor,"DEP")
            menu_opciones.mensaje_pantalla("-","Deposito realizado con exito")
        elif opc== 7:
            menu_opciones.mensaje_pantalla("-", "retirar de cuentas")
            cuenta = input("digite numero de cuenta para realizar retiro: ")
            pos = cb.buscar_cuenta(lista, cuenta)
            if pos == -1:
                menu_opciones.mensaje_pantalla("*", "Cuenta no existe")
                continue
            valor = float(input("Digite el valor del retiro: "))
            cb.retirar(lista, pos, valor, "RET")
            menu_opciones.mensaje_pantalla("-", "retiro realizado con exito")
        elif opc==8:
            menu_opciones.mensaje_pantalla("-", "transferencia  de cuentas")
            cuenta = input("Digite numero de cuenta origen: ")
            pos = cb.buscar_cuenta(lista, cuenta)
            if pos == -1:
                menu_opciones.mensaje_pantalla("*", "Cuenta no existe")
                continue
            valor = float(input("Digite valor a transferir: "))
            cb.transferir(lista, pos, valor, "TRF")
            menu_opciones.mensaje_pantalla("-", "Transferencia realizada con exito")

            #seccion 3

        #salir del menu
        else:
            menu_opciones.mensaje_pantalla("+","Gracias por usar la aplicación")
            break
    else:
        menu_opciones.mensaje_pantalla("*","Opción Incorrecta")
