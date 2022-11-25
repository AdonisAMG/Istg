from tkinter import *
from tkinter import font,messagebox
from proyecto.imagenes.rutas_imagenes import Tool
from proyecto.presentacion.confirmacion_transaccion import FrmConfirmarTransaccion
from proyecto.negocios.Cliente import Cliente
from proyecto.negocios.Cuenta import Cuenta

class FrmTransaccion(Frame):
    def __init__(self,master=None,titulo=None,accion=None,cliente=None):
    #def crear_ventana(self,master=None,titulo=None,accion=None,datos=None):
        super().__init__(master)
        self.titulo=titulo
        self.master = master
        self.accion=accion
        #self.datos=datos
        self.cliente=cliente
        self.cta_id=0
        #self.resultado=False
        #self.email_registrado=email
        self.numero_cta=StringVar()
        self.saldo_disp = StringVar()
        self.tipo_transaccion=StringVar()
        self.correo_electronico = StringVar()
        self.celular = StringVar()
        self.cedula = StringVar()
        self.lbl_fonts = font.Font(family="Calibri", size=9, weight="bold")
        self.lbl_entrys = font.Font(family="Calibri", size=14, weight="bold")
        self.tools = Tool(self.master)

        self.master.title(titulo)
        self.master.iconbitmap(self.tools.imagen_icono)
        self.crear_widgets()


    def continuar(self):
        if self.accion=="DEPOSITAR":
            self.depositar()

        if self.accion=="RETIRAR":
            messagebox.showinfo(self.titulo,"En desarrollo.....")

        if self.accion == "TRANSFERIR":
            messagebox.showinfo(self.titulo,"En desarrollo.....")


    def depositar(self):
        numero_cta = self.numero_cta.get()
        saldo_disp = self.saldo_disp.get()
        monto = self.txt_monto_transaccion.get()

        if not monto:
            messagebox.showwarning(self.titulo, "Digite el monto a retirar, por favor!!")
            return False

        monto=float(monto)
        saldo = float(saldo_disp) + float(monto)

        #verificar la transaccion a traves de la  clave temp. enviada al correo registrado
        ventana=Toplevel(self.master)
        app=FrmConfirmarTransaccion()
        resultado=app.crear_ventana(master=ventana,titulo="Confirmar Datos",accion="REGISTRAR",email=self.txt_email.get())

        if not resultado:
            messagebox.showwarning(self.titulo,"No se puede seguir con la transaccion!!")
            return False


        cuentas = Cuenta()
        if not cuentas.depositar_by_cta(self.cta_id,numero_cta, monto,saldo):
            messagebox.showwarning(self.titulo, "Ocurrio un error al momento de realizar la transacción!!")
            return False

        messagebox.showinfo(self.titulo, "Deposito realizado con éxito!!")
        if messagebox.askquestion(self.titulo,"Desean realizar otra transacción:  ")=="no":
            self.master.destroy()


    def cancelar(self):
        if messagebox.askquestion(title=self.titulo, message="Está seguro de cancelar la transacción Sí / No") == "yes":
            self.master.destroy()


    def validate_entry(self,text):
        # print(text,"largo codigo: ",len(self.txt_codigo_temp.get()))
        # if len(self.txt_codigo_temp.get())>3:
        #     messagebox.showinfo("parar")
        #     text = ""
        #     return text
        return text.isdecimal()

    def crear_widgets(self):
        fila_grid = 1

        # ZONA DE IDENTIFICACION
        self.lbl_frm_ident = LabelFrame(self.master, text="Identificación",
                                        font=self.lbl_fonts,
                                        width=60, height=100)
        self.lbl_frm_ident.grid(row=fila_grid, column=0, padx=20, pady=5)
        fila_grid += 1

        self.lbl1 = Label(self.lbl_frm_ident, text="Correo Electrónico", width=26, anchor="w", bg="gray", fg="black")
        self.lbl1.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_email = Entry(self.lbl_frm_ident, width=62, state="disabled", textvariable=self.correo_electronico)
        self.txt_email.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1

        self.lbl2 = Label(self.lbl_frm_ident, text="# de Celular", width=26, anchor="w", bg="gray", fg="black")
        self.lbl2.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_celular = Entry(self.lbl_frm_ident, width=62, state="disabled", textvariable=self.celular)
        self.txt_celular.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1

        self.lbl3 = Label(self.lbl_frm_ident, text="# de Cédula", width=26, anchor="w", bg="gray", fg="black")
        self.lbl3.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_cedula = Entry(self.lbl_frm_ident, width=62, state="disabled", textvariable=self.cedula)
        self.txt_cedula.grid(row=fila_grid, column=2, padx=15, pady=1)
        fila_grid += 1

        #
        self.labelframe = LabelFrame(self.master, text="Transacción",
                                     font=self.lbl_fonts,
                                     width=60, height=100)
        self.labelframe.grid(row=fila_grid, column=0, padx=20, pady=10)
        fila_grid += 1

        self.lbl3_1 = Label(self.labelframe, text="Número de Cuenta:", width=26, anchor="w", bg="gray", fg="black")
        self.lbl3_1.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_numero_cta = Entry(self.labelframe, width=37, font=self.lbl_entrys, state="readonly",
                                    textvariable=self.numero_cta)
        self.txt_numero_cta.grid(row=fila_grid, column=2, columnspan=2, padx=15, pady=2, ipady=2)
        fila_grid += 1

        self.lbl4 = Label(self.labelframe, text="Saldo Disponible", width=26, anchor="w", bg="gray", fg="black")
        self.lbl4.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_saldo_disp = Entry(self.labelframe, width=37,font=self.lbl_entrys,state="readonly",textvariable=self.saldo_disp)
        self.txt_saldo_disp.grid(row=fila_grid, column=2,columnspan=2, padx=15, pady=2,ipady=2)
        fila_grid += 1



        self.transaccion=""
        if self.accion=="DEPOSITAR":
            self.transaccion="Deposito en Cuenta Bancaria"
            self.mensaje_tipo_transaccion="Monto a Depositar"
        if self.accion=="RETIRAR":
            self.transaccion="Retiro de Cuenta Bancaria"
            self.mensaje_tipo_transaccion = "Monto a Retirar"
        if self.accion=="TRANSFERIR":
            self.transaccion="Transferencia de Cuentas Bancarias"
            self.mensaje_tipo_transaccion = "Monto a Transaferir"
        self.lbl5 = Label(self.labelframe, text="Tipo de Transacción: ", width=26, anchor="w", bg="gray", fg="black")
        self.lbl5.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_transaccion = Entry(self.labelframe, width=62, state="disabled", textvariable=self.tipo_transaccion)
        self.txt_transaccion.grid(row=fila_grid, column=2, padx=15, pady=1)
        self.tipo_transaccion.set(self.transaccion)
        fila_grid += 1

        self.lbl6 = Label(self.labelframe, text=self.mensaje_tipo_transaccion, width=26, anchor="w", bg="gray", fg="black")
        self.lbl6.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_monto_transaccion = Entry(self.labelframe, width=62, state="normal")
        self.txt_monto_transaccion.grid(row=fila_grid, column=2, padx=15, pady=1)
        fila_grid += 1

        if self.accion == "TRANSFERIR":
            self.lbl7 = Label(self.labelframe, text="Cuenta a Transferir", width=26, anchor="w", bg="gray",
                              fg="black")
            self.lbl7.grid(row=fila_grid, column=1, padx=10, pady=2)
            self.txt_cta_transferir = Entry(self.labelframe, width=62, state="normal")
            self.txt_cta_transferir.grid(row=fila_grid, column=2, padx=15, pady=1)
            fila_grid += 1

        # zona de botones
        self.frame_botones = LabelFrame(self.master, text="Acciones",
                                        font=self.lbl_fonts,
                                        width=200, height=100)
        self.frame_botones.grid(row=fila_grid, column=0, padx=20, pady=10)
        fila_grid += 1

        self.boton_Continuar = Button(self.frame_botones, text="Continuar", width=60, height=38,
                                    image=self.tools.imagen_avanzar, compound=TOP,
                                    command=self.continuar)
        self.boton_Continuar.grid(row=fila_grid, column=2, padx=3, pady=2)

        self.boton_cancelar = Button(self.frame_botones, text="Cancelar", width=60, height=38,
                                   image=self.tools.imagen_descartar, compound=TOP,
                                   command=self.cancelar)
        self.boton_cancelar.grid(row=fila_grid, column=3, padx=3, pady=2)

        clientes=Cliente()
        cuentas=Cuenta()
        lista_cta=cuentas.consulta_saldo_disponible_by_cli(self.cliente)
        lista_datos_reg = clientes.consulta_datos_registro_by_cli(self.cliente)

        self.cta_id=lista_cta[0]
        self.numero_cta.set(lista_cta[1])
        self.saldo_disp.set(lista_cta[2])

        self.correo_electronico.set(lista_datos_reg[0])
        self.celular.set(lista_datos_reg[1])
        self.cedula.set(lista_datos_reg[2])
