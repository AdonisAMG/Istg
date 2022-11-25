from tkinter import *
from tkinter import font,messagebox
#from proyecto.negocios.usuario import Usuario
#from proyecto.presentacion.menu_principal import FrmMenuPrincipal
from proyecto.imagenes.rutas_imagenes import Tool
from proyecto.negocios.Cliente import Cliente

class FrmLogin(Frame):
    #def __init__(self,master=None,titulo=None):
    def crear_ventana(self,master=None,titulo=None):
        super().__init__(master)

        self.titulo=titulo
        self.lbl_fonts=font.Font(family="Calibri",size=12,weight="bold")
        self.lbl_entrys=font.Font(family="Calibri",size=18,weight="bold")
        self.resultado=False
        self.master=master
        self.tools=Tool(self.master)
        self.master.title(titulo)
        self.master.iconbitmap(self.tools.imagen_icono)
        self.crear_widgets()

        self.master.grab_set()
        self.master.wait_window(self.master)
        return self.resultado

    def abrir_menu_principal(self):
        usuario=self.txt_user.get()
        passwd=self.txt_password.get()

        if not usuario:
            messagebox.showwarning(self.titulo,"Digite el Usuario/Correo Electrónico por favor!!")
            return False

        if not passwd:
            messagebox.showwarning(self.titulo,"Digite el password!!")
            return False

        clientes=Cliente()
        resp=clientes.validar_login(usuario,passwd)
        if not resp:
            messagebox.showwarning(self.titulo,"Usuario / Password Incorrectos!!")
            return False

        messagebox.showinfo(self.titulo,"Credenciales correctas, Bienvenido a la aplicación de servicios bancarios")
        self.resultado=resp
        self.master.destroy()


    def crear_widgets(self):
        fila_grid=1

        self.labelframe=LabelFrame(self.master,text="Inicio de sesión",
                              font=self.lbl_fonts,
                              width=60,height=100)
        self.labelframe.grid(row=fila_grid,column=0,padx=20,pady=10)
        fila_grid = 1

        lbl_imagen=Label(self.labelframe,width=100,height=50,
                         image=self.tools.imagen_iniciar_sesion)
        lbl_imagen.grid(row=fila_grid,column=1,padx=5,pady=5)
        fila_grid += 1


        lbl1=Label(self.labelframe,text="Usuario / Correo Electrónico Registrado",
                       font=self.lbl_fonts,
                       width=40)
        lbl1.grid(row=fila_grid,column=1,padx=5,pady=5)
        fila_grid +=1

        self.txt_user=Entry(self.labelframe,width=28,font=self.lbl_entrys)
        self.txt_user.grid(row=fila_grid,column=1,padx=10,pady=8,ipady=5)
        fila_grid += 1

        lbl2=Label(self.labelframe,text="Password",width=30,font=self.lbl_fonts)
        lbl2.grid(row=fila_grid,column=1,padx=5,pady=5)
        fila_grid+=1

        self.txt_password=Entry(self.labelframe,width=28,font =self.lbl_entrys,show="*")
        self.txt_password.grid(row=fila_grid,column=1,padx=10,pady=5,ipady=5)
        fila_grid += 1

        self.btn_seguir=Button(self.labelframe,text="Iniciar Sesión  ",
                          image=self.tools.imagen_seguir,compound=RIGHT,
                          font=self.lbl_fonts,
                          command=self.abrir_menu_principal,
                          width=330)
        self.btn_seguir.grid(row=fila_grid,column=1,padx=5,pady=10)

        #solo para pruebas desde
        self.txt_user.insert(0,"juan")
        self.txt_password.insert(0,"1234")
        #hasta

# root=Tk()
# app=FrmLogin(master=root,titulo="Login")
# app.mainloop()


