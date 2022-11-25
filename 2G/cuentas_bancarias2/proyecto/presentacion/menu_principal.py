from tkinter import *
from tkinter import messagebox
from proyecto.imagenes.rutas_imagenes import Tool
from proyecto.presentacion.registrar_ahora import FrmRegistrarNuevaCta
from proyecto.presentacion.registro_datos import FrmRegistroDatos
from proyecto.presentacion.login import FrmLogin
from proyecto.presentacion.transacciones import FrmTransaccion
from proyecto.negocios.Cuenta import Cuenta

class FrmMenuPrincipal(Frame):
    def __init__(self,master=None,titulo=None):
        super().__init__(master)
        self.titulo = titulo
        self.id_sesion=False
        self.master=master
        self.tools=Tool(self.master)
        self.master.title(titulo)
        self.master.geometry("1000x600")
        self.master.resizable(False,False)
        self.master.iconbitmap(self.tools.imagen_icono)
        #print(self.tools.imagen_icono)
        self.crear_widgets()

    def depositar(self):
        if not self.id_sesion:
            messagebox.showwarning(self.titulo,"Para utilizar los servicios bancarios primero debe iniciar sesión con su usuario!!")
            return False

        root = Toplevel(self.master)
        app = FrmTransaccion(master=root, titulo="Transacciones Bancarias - Depositos", accion="DEPOSITAR",
                             cliente=self.id_sesion)
        app.mainloop()


    def retirar(self):
        if not self.id_sesion:
            messagebox.showwarning(self.titulo,
                                   "Para utilizar los servicios bancarios primero debe iniciar sesión con su usuario!!")
            return False

        root = Toplevel(self.master)
        app = FrmTransaccion(master=root, titulo="Transacciones Bancarias - Retiros", accion="RETIRAR",
                             cliente=self.id_sesion)
        app.mainloop()

    def transferir(self):
        dict_datos = {}
        dict_datos.setdefault("correo", "jojam200x@hotmail.com")
        dict_datos.setdefault("celular", "0999999941")
        dict_datos.setdefault("cedula", "0919999912")
        dict_datos.setdefault("id_usuario", "1")
        dict_datos.setdefault("id_cliente", "1")
        root = Toplevel(self.master)
        # app=FrmTransaccion(master=root,titulo="Transacciones Bancarias - Depositos",accion="DEPOSITAR",datos=dict_datos)
        # app=FrmTransaccion(master=root,titulo="Transacciones Bancarias - Retiros",accion="RETIRAR",datos=dict_datos)
        app = FrmTransaccion(master=root, titulo="Transacciones Bancarias - Transferencia", accion="TRANSFERIR",datos=dict_datos)
        app.mainloop()


    def abrir_cuentas(self):
        root=Toplevel(self.master)
        app=FrmRegistrarNuevaCta(master=root,titulo="Registrar Nueva Cuenta")

    def actualizar_datos(self):
        dict_datos = {}
        dict_datos.setdefault("correo", "jojam200x@hotmail.com")
        dict_datos.setdefault("celular", "0990147641")
        dict_datos.setdefault("cedula", "0919367912")
        dict_datos.setdefault("id_usuario", "1")
        dict_datos.setdefault("id_cliente", "1")

        root = Toplevel(self.master)
        app = FrmRegistroDatos()
        app.crear_ventana(master=root, titulo="Actualización de Datos", accion="ACTUALIZAR",datos=dict_datos)
        pass

    def iniciar_sesion(self):
        root=Toplevel(self.master)
        app=FrmLogin()
        self.id_sesion=app.crear_ventana(master=root,titulo="Login")
        if self.id_sesion != False:
            self.habilitar_opc_menu("normal","normal","normal","normal","disabled","normal","disabled")
        #messagebox.showinfo(self.titulo,"id cliente: " + str(self.id_sesion))

    def salir(self):
        if messagebox.askquestion(self.titulo, "Desea Salir: Sí/No ") == "yes":
            self.master.destroy()
        self.tools.mensaje_cerrar_ventana(self.titulo)

    def saldo_disponible(self):
        if not self.id_sesion:
            messagebox.showwarning(self.titulo,"Para utilizar los servicios bancarios primero debe iniciar sesión con su usuario!!")
            return False

        cuentas=Cuenta()
        lista_cuenta=cuentas.consulta_saldo_disponible_by_cli(self.id_sesion)
        if lista_cuenta == -1:
            messagebox.showwarning(self.titulo,"""Ocurrio un error al consultar su Saldo Disponible,
            intente de nuevo mas tarde.""")
            return False

        messagebox.showinfo(self.titulo,f"""EL SALDO DISPONIBLE DE LA CUENTA: {lista_cuenta[1]} 
        ES:  ${lista_cuenta[2]:.2f}""")

    def movimientos_bancarios(self):
        pass


    def habilitar_opc_menu(self,banca_virtual,transacciones,reportes,salir,cuenta_nueva,actualizar_datos,iniciar_sesion):
        self.menubar.entryconfig(index=1, state=banca_virtual)
        self.menubar.entryconfig(index=2, state=transacciones)
        self.menubar.entryconfig(index=3, state=reportes)
        self.menubar.entryconfig(index=4, state=salir)
        self.menu_banca_virtual.entryconfig(index=0, state=cuenta_nueva)
        self.menu_banca_virtual.entryconfig(index=1, state=actualizar_datos)
        self.menu_banca_virtual.entryconfig(index=2, state=iniciar_sesion)

    def crear_widgets(self):

        #BARRA DE MENUS
        self.menubar=Menu(self.master)

        #MENU BANCA VIRTUAL
        self.menu_banca_virtual=Menu(self.menubar,tearoff=0)
        self.menu_banca_virtual.add_command(label="Abrir Nueva Cuenta",
                                            command=self.abrir_cuentas,
                                            image=self.tools.imagen_abrir_cuenta,compound=RIGHT)
        self.menu_banca_virtual.add_command(label="Actualizar Datos",
                                            command=self.actualizar_datos,
                                            image=self.tools.imagen_actualizar,compound=RIGHT)
        self.menu_banca_virtual.add_command(label="Iniciar Sesión",
                                            command=self.iniciar_sesion,
                                            image=self.tools.imagen_iniciar_sesion,compound=RIGHT)
        self.menubar.add_cascade(label="Menu Banca Virtual",menu=self.menu_banca_virtual)


        # MENU TRANSACCIONES
        self.menu_transacciones_banc = Menu(self.menubar, tearoff=0)
        self.menu_transacciones_banc.add_command(label="Depositar        ",
                                                 command=self.depositar,
                                                 image=self.tools.imagen_depositos,compound=RIGHT)
        self.menu_transacciones_banc.add_command(label="Retirar          ",
                                                 command=self.retirar,
                                                 image = self.tools.imagen_retiros, compound = RIGHT)
        self.menu_transacciones_banc.add_command(label="Transferir   ",
                                                 command=self.transferir,
                                                 image=self.tools.imagen_transferencia,compound=RIGHT)
        self.menubar.add_cascade(label="Menu Transacciones", menu=self.menu_transacciones_banc)

        #MENU REPORTES
        self.menu_reportes = Menu(self.menubar, tearoff=0)
        self.menu_reportes.add_command(label="Saldo Disponible",
                                    command=self.saldo_disponible,
                                    image=self.tools.imagen_salir, compound=RIGHT)
        self.menu_reportes.add_command(label="Movimientos Bancarios",
                                       command=self.movimientos_bancarios,
                                       image=self.tools.imagen_salir, compound=RIGHT)
        self.menubar.add_cascade(label="Menu Reportes", menu=self.menu_reportes)

        # MENU SALIR
        self.menu_salir = Menu(self.menubar, tearoff=0)
        self.menu_salir.add_command(label="cerrar sesion y salir",
                                    command=self.salir,
                                    image=self.tools.imagen_salir, compound=RIGHT)
        self.menubar.add_cascade(label="Salir", menu=self.menu_salir)

        #UBICANDO EL MENU EN LA VENTANA
        self.master.config(menu=self.menubar)
        self.habilitar_opc_menu("normal", "disabled", "disabled", "disabled","normal","disabled","normal")



root=Tk()
app=FrmMenuPrincipal(master=root,titulo="Servicios Bancarios")
app.mainloop()