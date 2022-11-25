from tkinter import *
from tkinter import font,messagebox
from proyecto.imagenes.rutas_imagenes import Tool
from proyecto.negocios.Correo import EnvioEmails
import time
from random import randrange

class FrmConfirmarTransaccion(Frame):
    #def __init__(self,master=None,titulo=None,accion=None,email=None):
    def crear_ventana(self,master=None,titulo=None,accion=None,email=None):
        super().__init__(master)
        self.titulo=titulo
        self.master = master
        self.accion=accion
        self.resultado=False
        self.clave_temporal=0
        self.email_registrado=email
        self.email=StringVar()
        self.lbl_fonts = font.Font(family="Calibri", size=9, weight="bold")
        self.lbl_entrys = font.Font(family="Calibri", size=14, weight="bold")
        self.tools = Tool(self.master)

        self.master.title(titulo)
        self.master.iconbitmap(self.tools.imagen_icono)
        self.crear_widgets()
        self.enviar_correo()
        self.master.grab_set()
        self.master.wait_window(self.master)
        return self.resultado

    def enviar_correo(self):
        # probar desde
        fecha = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        self.clave_temporal = randrange(1000, 9999)

        mensage = """Registramos solicitud de clave de seguridad
               temporal el:  {}
                 La clave asignada es {}""".format(fecha, self.clave_temporal)

        correo_origen = "pruebas.correos.poo.2g2h@gmail.com"
        password = "Pcorreos123456"
        destinatario = "jojam200x@hotmail.com"
        asunto = "Solicitud de Transaccion"

        msg_errores = {}
        envio_correo = EnvioEmails(correo_origen, password, destinatario, asunto, mensage)
        value = envio_correo.enviar_correo(msg_errores)
        print(value)

        if not value:
            print("**** Error ****: ")
            print(msg_errores["ERROR_1"])
            print(msg_errores["ERROR_2"])
            print(msg_errores["ERROR_3"])
            messagebox.showerror(self.titulo, msg_errores)
            self.resultado=False
            self.master.destroy()
        # else:
        #     print("Correo Enviado con exito")
        #     self.resultado = True

        # hasta

    def continuar(self):
        if self.accion=="REGISTRAR":

          if self.clave_temporal == int(self.txt_codigo_temp.get()):
              messagebox.showinfo(self.titulo,"La solicitud de clave de seguridad temporal es CORRECTA")
              self.resultado = True
          else:
              messagebox.showwarning(self.titulo,"La solicitud de clave de seguridad temporal es INCORRECTA")
              self.resultado=False
          self.master.destroy()

        if self.accion=="ACTUALIZAR":
            self.resultado = True
            self.master.destroy()

    def cancelar(self):
        self.resultado = False
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

        self.labelframe = LabelFrame(self.master, text="Confirmar Transacción",
                                     font=self.lbl_fonts,
                                     width=60, height=100)
        self.labelframe.grid(row=fila_grid, column=0, padx=20, pady=10)
        fila_grid += 1

        self.lbl1 = Label(self.labelframe, text="Correo Electrónico", width=15, anchor="w", bg="gray", fg="black")
        self.lbl1.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_email = Entry(self.labelframe, width=30,font=self.lbl_entrys,state="readonly",textvariable=self.email)
        self.txt_email.grid(row=fila_grid, column=2,columnspan=2, padx=10, pady=2,ipady=2)
        fila_grid += 1

        self.lbl2 = Label(self.labelframe, text="Código Temporal", width=15, anchor="w", bg="gray", fg="black")
        self.lbl2.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_codigo_temp = Entry(self.labelframe, width=30,font=self.lbl_entrys,
                                     validate="key",
                                     validatecommand=(self.master.register(self.validate_entry), "%S")
                                     )
        self.txt_codigo_temp.grid(row=fila_grid, column=2,columnspan=3, padx=10, pady=2,ipady=2)
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

        self.email.set(self.email_registrado)



# root=Tk()
# app=FrmConfirmarTransaccion()
# app.crear_ventana(master=root,titulo="Confirmar Datos",accion="REGISTRAR")
# app.mainloop()