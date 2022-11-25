from tkinter import *
from tkinter import font,messagebox
from proyecto.imagenes.rutas_imagenes import Tool
from proyecto.presentacion.confirmacion_transaccion import FrmConfirmarTransaccion
from proyecto.negocios.Cliente import Cliente
from proyecto.negocios.Cuenta import  Cuenta
from random import randrange

class FrmRegistroDatos(Frame):
    #def __init__(self,master=None,titulo=None,accion=None):
    def crear_ventana(self,master=None,titulo=None,accion=None,correo=None,celular=None,cedula=None):
        super().__init__(master)
        self.titulo=titulo
        self.master = master
        self.accion=accion
        #self.datos=datos

        self.correo_reg=correo
        self.celular_reg=celular
        self.cedula_reg=cedula

        self.correo_electronico=StringVar()
        self.celular=StringVar()
        self.cedula=StringVar()

        self.numero_cta=StringVar()
        self.tipo_cta=StringVar()
        self.saldo_cta=StringVar()

        self.lbl_fonts = font.Font(family="Calibri", size=9, weight="bold")
        self.lbl_entrys = font.Font(family="Calibri", size=9, weight="bold")
        self.tools = Tool(self.master)

        self.master.title(titulo)
        self.master.geometry("770x740+268+25")
        self.master.iconbitmap(self.tools.imagen_icono)
        self.crear_widgets()
        if self.accion=="REGISTRAR":
            self.master.grab_set()
            self.master.wait_window(self.master)
            return True

    #RETORNA FALSE  SI LOS CAMPOS DE TEXTO ESTAN LISTOS
    #               PARA GUARDAR/ACTUALIZAR
    #        TRUE   SI LOS CAMPOS DE TEXTO ESTAN VACIOS
    def validar_valores(self):
        mensaje = "Digite los campos obligatorios (*) "
        if not self.txt_nombres.get():
            messagebox.showwarning(self.titulo,mensaje + ": Nombres, por favor!!")
            self.txt_nombres.focus_set()
            return True

        if not self.txt_apellidos.get():
            messagebox.showwarning(self.titulo,mensaje)
            self.txt_apellidos.focus_set()
            return True

        if not self.txt_nombres_contacto.get():
            messagebox.showwarning(self.titulo, mensaje)
            self.txt_nombres_contacto.focus_set()
            return True

        if not self.txt_tlf_contacto.get():
            messagebox.showwarning(self.titulo, mensaje)
            self.txt_tlf_contacto.focus_set()
            return True

        if not self.txt_calle_princ.get():
            messagebox.showwarning(self.titulo, mensaje)
            self.txt_calle_princ.focus_set()
            return True

        if not self.txt_numeracion.get():
            messagebox.showwarning(self.titulo, mensaje)
            self.txt_numeracion.focus_set()
            return True

        valor=self.txt_referencia_domicilio.get(1.0,END)
        #print("referencia: ",len(valor))
        if len(valor)==1:
            messagebox.showwarning(self.titulo, mensaje)
            #self.txt_referencia_domicilio.focus_set()
            return True

        if not self.txt_nombres_contacto.get():
            messagebox.showwarning(self.titulo, mensaje)
            self.txt_nombres_contacto.focus_set()
            return True

        if not self.txt_usuario.get():
            messagebox.showwarning(self.titulo, mensaje)
            self.txt_usuario.focus_set()
            return True

        if not self.txt_passwd.get():
            messagebox.showwarning(self.titulo, mensaje)
            self.txt_passwd.focus_set()
            return True



    def ejecutar(self):
        # root = Toplevel(self.master)
        # app = FrmConfirmarTransaccion(root)
        # resp_confir = app.crear_ventana(master=root, titulo="Confirmación de Transacción", accion=self.accion,email=self.txt_email.get())

        # messagebox.showinfo(self.titulo,"valor devuelto: " + str(resp_confir))
        # print("codigo temporal: ",resp_confir)
        if self.accion=="REGISTRAR":
            self.registrar()
        elif self.accion=="ACTUALIZAR":
            self.actualizar()

    def actualizar(self):
        messagebox.showinfo(title=self.titulo,message="Datos actualizados con Exito")

    def registrar(self):
        #validando que las cajas de texto no esten vacias
        if self.validar_valores():return False

        #validando que el usuario no este registrado en la tabla clientes
        # clientes=Cliente()
        # if not clientes.consulta_usuario(self.txt_usuario.get()):
        #
        #     messagebox.showwarning(self.titulo, "Ya existe un cliente con ese usuario!!")
        #     return False
        #
        # cliente_id=clientes.ingresar_cliente(self.txt_email.get(),self.txt_celular.get(),
        #                           self.txt_cedula.get(),self.txt_nombres.get(),
        #                           self.txt_apellidos.get(),self.txt_fecha_nac.get(),
        #                           self.txt_nombres_contacto.get(),self.txt_tlf_contacto,
        #                           self.txt_calle_princ.get(),self.txt_numeracion,
        #                           self.txt_usuario.get(),self.txt_passwd.get())
        # if not cliente_id:
        #     messagebox.showwarning(self.titulo,"Ocurrio un error al guardar el cliente!!!")
        #     return False

        cuentas=Cuenta()
        #cuentas.crear_cuenta(self.txt_numero_cta.get(),self.cliente_id,self.txt_clave_cta.get())
        cuentas.crear_cuenta(self.txt_numero_cta.get(), 5, self.txt_clave_cta.get())
        messagebox.showinfo(self.titulo,"Cliente Registrado con Exito!!")


    def cancelar(self):
        if messagebox.askquestion(title=self.titulo,message="Está seguro de cancelar el Registro Sí / No")=="yes":
            self.master.destroy()

    def tocar(self):
        messagebox.showinfo("salio")

    def cuandoEscriba(self,event):
        if event.char.isdigit():

            texto = self.txt_fecha_nac.get()
            letras = 0

            #print("largo entry: ", len(texto))
            if len(texto) > 9: return "break"

            for i in texto:
                letras += 1

            if letras == 2:
                self.txt_fecha_nac.insert(2, "/")
            elif letras == 5:
                self.txt_fecha_nac.insert(5, "/")
        else:
            return "break"

    def crear_widgets(self):
        #print(self.accion)
        fila_grid = 1

        # print(self.datos["correo"])
        # print(self.datos["celular"])
        # print(self.datos["cedula"])

        #ZONA DE IDENTIFICACION
        self.lbl_frm_ident = LabelFrame(self.master, text="Identificación",
                                     font=self.lbl_fonts,
                                     width=60, height=100)
        self.lbl_frm_ident.grid(row=fila_grid, column=0, padx=20, pady=5)
        fila_grid += 1

        self.lbl1 = Label(self.lbl_frm_ident, text="Correo Electrónico", width=26, anchor="w", bg="gray", fg="black")
        self.lbl1.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_email = Entry(self.lbl_frm_ident, width=80,state="disabled",textvariable=self.correo_electronico)
        self.txt_email.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1

        self.lbl2 = Label(self.lbl_frm_ident, text="# de Celular", width=26, anchor="w", bg="gray", fg="black")
        self.lbl2.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_celular = Entry(self.lbl_frm_ident, width=80,state="disabled",textvariable=self.celular)
        self.txt_celular.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1

        self.lbl3 = Label(self.lbl_frm_ident, text="# de Cédula", width=26, anchor="w", bg="gray", fg="black")
        self.lbl3.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_cedula = Entry(self.lbl_frm_ident, width=80,state="disabled",textvariable=self.cedula)
        self.txt_cedula.grid(row=fila_grid, column=2, padx=15, pady=1)
        fila_grid += 1

        # ZONA DE DATOS PERSONALES
        self.lbl_frm_dat_pers = LabelFrame(self.master, text="Datos Personales",
                                     font=self.lbl_fonts,
                                     width=60, height=100)
        self.lbl_frm_dat_pers.grid(row=fila_grid, column=0, padx=20, pady=2)
        fila_grid += 1

        self.lbl4 = Label(self.lbl_frm_dat_pers, text="*Nombres:", width=26, anchor="w", bg="gray", fg="black")
        self.lbl4.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_nombres = Entry(self.lbl_frm_dat_pers, width=80)
        self.txt_nombres.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1

        self.lbl5 = Label(self.lbl_frm_dat_pers, text="*Apellidos:", width=26, anchor="w", bg="gray", fg="black")
        self.lbl5.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_apellidos = Entry(self.lbl_frm_dat_pers, width=80)
        self.txt_apellidos.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1

        self.lbl6 = Label(self.lbl_frm_dat_pers, text="*Fecha de Nacimiento:", width=26, anchor="w", bg="gray", fg="black")
        self.lbl6.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_fecha_nac = Entry(self.lbl_frm_dat_pers, width=80)
        self.txt_fecha_nac.grid(row=fila_grid, column=2, padx=15, pady=2)

        self.txt_fecha_nac.bind("<Key>", self.cuandoEscriba)
        self.txt_fecha_nac.bind("<BackSpace>", lambda _: self.txt_fecha_nac.delete(END))


        fila_grid += 1

        self.lbl7 = Label(self.lbl_frm_dat_pers, text="Estado Civil:", width=26, anchor="w", bg="gray",fg="black")
        self.lbl7.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_est_civil = Entry(self.lbl_frm_dat_pers, width=80)
        self.txt_est_civil.grid(row=fila_grid, column=2, padx=15, pady=4)
        fila_grid += 1


        # ZONA DE CONTACTOS
        self.lbl_frm_contactos = LabelFrame(self.master, text="Contactos",
                                     font=self.lbl_fonts,
                                     width=60, height=100)
        self.lbl_frm_contactos.grid(row=fila_grid, column=0, padx=20, pady=2)
        fila_grid += 1

        self.lbl8 = Label(self.lbl_frm_contactos, text="*Nombres completos de Contacto:", width=26, anchor="w", bg="gray", fg="black")
        self.lbl8.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_nombres_contacto = Entry(self.lbl_frm_contactos, width=80)
        self.txt_nombres_contacto.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1

        self.lbl9 = Label(self.lbl_frm_contactos, text="*Telefonos completos de Contacto:", width=26, anchor="w", bg="gray", fg="black")
        self.lbl9.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_tlf_contacto = Entry(self.lbl_frm_contactos, width=80)
        self.txt_tlf_contacto.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1

        self.lbl10 = Label(self.lbl_frm_contactos, text="Parentezco de Contacto:", width=26, anchor="w", bg="gray", fg="black")
        self.lbl10.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_parentezco_contacto = Entry(self.lbl_frm_contactos, width=80)
        self.txt_parentezco_contacto.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1

        # ZONA DE RESIDENCIA
        self.lbl_frm_resid = LabelFrame(self.master, text="*Residencia",
                                     font=self.lbl_fonts,
                                     width=60, height=100)
        self.lbl_frm_resid.grid(row=fila_grid, column=0, padx=20, pady=2)
        fila_grid += 1

        self.lbl11 = Label(self.lbl_frm_resid, text="*Calle Principal:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl11.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_calle_princ = Entry(self.lbl_frm_resid, width=20)
        self.txt_calle_princ.grid(row=fila_grid, column=2, padx=15, pady=2)
        #fila_grid += 1

        self.lbl12 = Label(self.lbl_frm_resid, text="*Numeracion:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl12.grid(row=fila_grid, column=3, padx=10, pady=2)
        self.txt_numeracion = Entry(self.lbl_frm_resid, width=20)
        self.txt_numeracion.grid(row=fila_grid, column=4, padx=15, pady=2)
        fila_grid += 1

        self.lbl13= Label(self.lbl_frm_resid, text="Calle Secundaria:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl13.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_calle_sec = Entry(self.lbl_frm_resid, width=20)
        self.txt_calle_sec.grid(row=fila_grid, column=2, padx=15, pady=2)

        self.lbl15 = Label(self.lbl_frm_resid, text="Telefono Domicilio:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl15.grid(row=fila_grid, column=3, padx=10, pady=2)
        self.txt_tlf_domicilio = Entry(self.lbl_frm_resid, width=20)
        self.txt_tlf_domicilio.grid(row=fila_grid, column=4, padx=15, pady=2)
        fila_grid += 1

        self.lbl14 = Label(self.lbl_frm_resid, text="*Referencia:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl14.grid(row=fila_grid, column=1, padx=10, pady=2)
        # self.txt_referencia_domicilio = Entry(self.lbl_frm_resid, width=80)
        # self.txt_referencia_domicilio.grid(row=fila_grid, column=2,columnspan="3", padx=15, pady=2)
        self.txt_referencia_domicilio = Text(self.lbl_frm_resid,width=60, height=2)
        self.txt_referencia_domicilio.grid(row=fila_grid, column=2,columnspan="3", padx=15, pady=2)
        fila_grid += 1

        # ZONA DE CUENTA BANCARIA
        self.lbl_frm_user = LabelFrame(self.master, text="Datos de la Cuenta",
                                       font=self.lbl_fonts,
                                       width=60, height=100)
        self.lbl_frm_user.grid(row=fila_grid, column=0, padx=20, pady=4)
        fila_grid += 1

        self.lbl16 = Label(self.lbl_frm_user, text="# de Cuenta:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl16.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_numero_cta = Entry(self.lbl_frm_user, width=20,state="disabled",textvariable=self.numero_cta)
        self.txt_numero_cta.grid(row=fila_grid, column=2, padx=15, pady=2)

        self.lbl17 = Label(self.lbl_frm_user, text="Saldo de Cuenta:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl17.grid(row=fila_grid, column=3, padx=10, pady=2)
        self.txt_saldo_cta = Entry(self.lbl_frm_user, width=20,state="disabled",textvariable=self.saldo_cta)
        self.txt_saldo_cta.grid(row=fila_grid, column=4, padx=15, pady=2)
        fila_grid += 1

        self.lbl18 = Label(self.lbl_frm_user, text="Tipo de Cuenta:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl18.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_tipo_cta = Entry(self.lbl_frm_user, width=20,state="disabled",textvariable=self.tipo_cta)
        self.txt_tipo_cta.grid(row=fila_grid, column=2, padx=15, pady=2)

        self.lbl19 = Label(self.lbl_frm_user, text="*Clave:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl19.grid(row=fila_grid, column=3, padx=10, pady=2)
        self.txt_clave_cta = Entry(self.lbl_frm_user, width=20)
        self.txt_clave_cta.grid(row=fila_grid, column=4, padx=15, pady=2)
        fila_grid += 1

        # ZONA DE USUARIOS
        self.lbl_frm_user = LabelFrame(self.master, text="Datos de Usuario",
                                     font=self.lbl_fonts,
                                     width=60, height=100)
        self.lbl_frm_user.grid(row=fila_grid, column=0, padx=20, pady=4)
        fila_grid += 1

        self.lbl20 = Label(self.lbl_frm_user, text="*Usuario:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl20.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_usuario = Entry(self.lbl_frm_user, width=20)
        self.txt_usuario.grid(row=fila_grid, column=2, padx=15, pady=2)
        #fila_grid += 1

        self.lbl21 = Label(self.lbl_frm_user, text="*Password:", width=26, anchor="w", bg="gray",
                           fg="black")
        self.lbl21.grid(row=fila_grid, column=3, padx=10, pady=2)
        self.txt_passwd = Entry(self.lbl_frm_user, width=20,show="*")
        self.txt_passwd.grid(row=fila_grid, column=4, padx=15, pady=2)
        fila_grid += 1

        #imagen_defecto
        self.lbl22 = Label(self.lbl_frm_user, text="Imagen Asociativa:", width=26, anchor="w", bg="gray",fg="black")
        self.lbl22.grid(row=fila_grid, column=1, padx=10, pady=2)
        lbl_imagen = Label(self.lbl_frm_user, width=210, height=100,
                           image=self.tools.imagen_defecto)
        lbl_imagen.grid(row=fila_grid, column=2,columnspan="2", padx=15, pady=1)
        fila_grid += 1


        ######################################
        ##  ZONA DE BOTONES
        ######################################
        self.frame_botones = LabelFrame(self.master, text="Acciones",
                                        font=self.lbl_fonts,
                                        width=200, height=100)
        self.frame_botones.grid(row=fila_grid, column=0, padx=20, pady=3)
        fila_grid += 1

        self.boton_registrar = Button(self.frame_botones, text="Registrar", width=60, height=38,
                                    image=self.tools.imagen_registrar, compound=TOP,
                                    command=self.ejecutar)
        self.boton_registrar.grid(row=fila_grid, column=2, padx=3, pady=2)

        self.boton_cancelar = Button(self.frame_botones, text="Cancelar", width=60, height=38,
                                   image=self.tools.imagen_descartar, compound=TOP,
                                   command=self.cancelar)
        self.boton_cancelar.grid(row=fila_grid, column=3, padx=3, pady=2)

        cuentas=Cuenta()
        if self.accion=="REGISTRAR":
            self.correo_electronico.set(self.correo_reg)
            self.celular.set(self.celular_reg)
            self.cedula.set(self.cedula_reg)

            num_cta=cuentas.generar_numero_cuenta()
            self.numero_cta.set(num_cta)
            self.saldo_cta.set("0")
            self.tipo_cta.set("AHORRO")
            clave = randrange(1000, 9999)
            self.txt_clave_cta.insert(0,clave)

            from datetime import datetime
            fecha=datetime.today().strftime('%Y-%m-%d %H:%M')
            print(fecha)

# root=Tk()
# app=FrmRegistroDatos()
# app.crear_ventana(master=root,titulo="Registro de Datos",accion="REGISTRAR")
# app.mainloop()