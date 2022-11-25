# rutas_images = {}
# rutas_images.setdefault("ICONO",
#                         "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\compras.ico")
# rutas_images.setdefault("LOGIN",
#                           "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\login_3_96.png")
# rutas_images.setdefault("INICIO_SESION",
#                           "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\Login_inicio.png")
# rutas_images.setdefault("GUARDAR",
#                         "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\guardar.png")
# rutas_images.setdefault("BUSCAR",
#                           "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\buscar.png")
# rutas_images.setdefault("ACTUALIZAR",
#                           "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\actualizar.png")
# rutas_images.setdefault("ELIMINAR",
#                           "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\eliminar.png")
# rutas_images.setdefault("DESCARTAR",
#                           "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\descartar.png")
# rutas_images.setdefault("CERRAR",
#                           "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\cerrar.png")


from tkinter import messagebox,PhotoImage
class Tool:
    def __init__(self,master):
        self.master=master

        self.imagen_icono =          "C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\bancos.ico"
        self.imagen_defecto =        PhotoImage(file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\imagen_por_defecto.png")
        self.imagen_transferencia =  PhotoImage(file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\transfer2.png")
        self.imagen_depositos =      PhotoImage(file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\depositos.png")
        self.imagen_retiros =        PhotoImage(file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\retiros3.png")
        self.imagen_salir = PhotoImage(
            file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\cerrar_sesion2.png")
        # self.imagen_iniciar_sesion = PhotoImage(
        #     file="C:\\Users\\JOHN\\Desktop\\cuentas_bancarias\\proyecto\\imagenes\\iniciar_sesion2.png")

        self.imagen_iniciar_sesion = PhotoImage(
            file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\usuarios.png")

        self.imagen_actualizar = PhotoImage(
            file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\actualizar2.png")
        self.imagen_abrir_cuenta = PhotoImage(
            file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\abrir_cuenta2.png")

        self.imagen_descartar =     PhotoImage(file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\descartar.png")

        self.imagen_registrar_datos = PhotoImage(
            file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\registrar_datos.png")

        self.imagen_seguir = PhotoImage(
            file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\Login_inicio.png")

        self.imagen_avanzar = PhotoImage(
            file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\avanzar.png")

        self.imagen_registrar = PhotoImage(
            file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\registrar.png")

        self.imagen_verificar_reg = PhotoImage(
            file="C:\\Users\\Familia Merchan\\Desktop\\cuentas_bancarias2\\proyecto\\imagenes\\verificar_registro.png")
        #self.imagen_iniciar_sesion = PhotoImage(file="C:\\Users\\JOHN\\Desktop\\cuentas_bancarias\\proyecto\\imagenes\\login_3_96.png")

        #self.imagen_icono =         "C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\compras.ico"

        #self.iniciar_sesion=        PhotoImage(file="C:\\Users\\JOHN\\Desktop\\cuentas_bancarias\\proyecto\\presentacion\\imagenes\\iniciar_sesion6.png")
        ##self.iniciar_sesion = PhotoImage(file="iniciar_sesion6.png")


        #self.imagen_icono=          "compras.ico"
        # self.imagen_iniciar_sesion= PhotoImage(file="C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\login_3_96.png")
        # self.imagen_seguir=         PhotoImage(file="C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\Login_inicio.png")
        # self.imagen_guardar =       PhotoImage(file="C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\guardar.png")
        # self.imagen_buscar =        PhotoImage(file="C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\buscar.png")
        # self.imagen_actualizar =    PhotoImage(file="C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\actualizar.png")
        # self.imagen_eliminar =      PhotoImage(file="C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\eliminar.png")
        # self.imagen_descartar =     PhotoImage(file="C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\descartar.png")
        # self.imagen_cerrar =        PhotoImage(file="C:\\Users\\JOHN\\Desktop\\ventas_productos_me\\proyecto\\imagenes\\cerrar.png")

    def mensaje_cerrar_ventana(self,titulo):
        if messagebox.askquestion(titulo,"Esta seguro de salir Sí/No: ") == "yes":
            print("yes")
            self.master.destroy()