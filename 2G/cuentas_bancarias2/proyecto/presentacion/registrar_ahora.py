from tkinter import *
from tkinter import font,messagebox,dialog
from proyecto.imagenes.rutas_imagenes import Tool
from proyecto.presentacion.registro_datos import FrmRegistroDatos
from proyecto.negocios.Cliente import Cliente

class FrmRegistrarNuevaCta(Frame):
    def __init__(self,master=None,titulo=None):
        super().__init__(master)
        self.master = master
        self.master.title(titulo)
        self.crear_widgets()


    def crear_widgets(self):
        fila_grid = 1

        self.labelframe = LabelFrame(self.master, text="Identificación", width=60, height=100)
        self.labelframe.grid(row=fila_grid, column=0, padx=20, pady=10)
        fila_grid += 1

        self.lbl1 = Label(self.labelframe, text="Correo Electrónico", width=26, anchor="w", bg="gray", fg="black")
        self.lbl1.grid(row=fila_grid, column=1, padx=10, pady=2)
        self.txt_email = Entry(self.labelframe, width=62)
        self.txt_email.grid(row=fila_grid, column=2, padx=15, pady=2)
        fila_grid += 1


root=Tk()
app=FrmRegistrarNuevaCta(master=root,titulo="Registrar Ahora")
app.mainloop()