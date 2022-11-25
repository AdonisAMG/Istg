from tkinter import *
from tkinter import messagebox
#from tkinter.ttk import Combobox

class Cliente:
    def crear_cliente(self, nombres, apellidos, direccion, cedula, correo, tlf_movil):
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.cedula = cedula
        self.correo = correo
        self.tlf_movil = tlf_movil
        self.estado = True


    def __str__(self):
        presentar = f"nombres: {self.nombres}\n" \
                    f"apellidos: {self.apellidos}\n" \
                    f"direccion: {self.direccion}\n" \
                    f"cedula: {self.cedula}\n" \
                    f"correo: {self.correo}\n" \
                    f"tlf_movil: {self.tlf_movil}"
        return presentar


def guardar():
    messagebox.showinfo("Formulario Clientes","Cliente Guardado con Exito",)
    #obtener info de un entry en este caso del entry de nombres
    nombres=entry1.get()
    print("Nombres: ",nombres)

    #apellido = input("digite apellidos")
    apellidos = entry2.get()
    print("Apellidos: ",apellidos)

    #capturar los otros entrys restantes
    direccion = entry3.get()
    print("Direccion: ",direccion)

    cedula = entry4.get()
    print("Cedula: ",cedula)

    correo = entry5.get()
    print("Apellidos: ",correo)

    tlf_movil = entry6.get()
    print("Tlf_movil: ",tlf_movil)


    #crear una instancia de la clase cliente
c=Cliente()
    #invocar al metodo crear_cliente y pasar los argumentos
c.crear_cliente('nombres', 'apellidos', 'direccion', 'cedula', 'correo', 'tlf_movil')
    #imprimir el objeto deseado
print(c)
print()




raiz=Tk()
raiz.title("Formulario de Clientes")
#raiz.iconbitmap("python_ico.ico")
frame=Frame(raiz,width="600",height=640,background="light gray")
frame.pack()

fila_grid=2

#NOMBRES
label1=Label(frame,text="Nombres:",anchor="w",width=40,background="gray",fg="white")
label1.grid(row=fila_grid,column=1,padx=15,pady=2)
entry1=Entry(frame,width=70)
entry1.grid(row=fila_grid,column=2,columnspan=2,padx=15,pady=1)
fila_grid+=1

#APELLIDOS
label2=Label(frame,text="apellidos:",anchor="w",width=40,background="gray",fg="white")
label2.grid(row=fila_grid,column=1,padx=15,pady=1)
entry2=Entry(frame,width=70)
entry2.grid(row=fila_grid,column=2,columnspan=2,padx=15,pady=1)
fila_grid+=1



# #RESIDENCIA
label4=Label(frame,text="Dirección de Residencia:",anchor="w",width=40,background="gray",fg="white")
label4.grid(row=fila_grid,column=1,padx=15,pady=1)
entry3=Entry(frame,width=70)
entry3.grid(row=fila_grid,column=2,columnspan=2,padx=15,pady=1)
fila_grid+=1
#

#
# #CEDULA,
label6=Label(frame,text="Cédula:",anchor="w",width=40,background="gray",fg="white")
label6.grid(row=fila_grid,column=1,padx=15,pady=1)
entry4=Entry(frame,width=70)
entry4.grid(row=fila_grid,column=2,columnspan=2,padx=15,pady=1)
fila_grid+=1
#
# #CORREO
label7=Label(frame,text="Correo:",anchor="w",width=40,background="gray",fg="white")
label7.grid(row=fila_grid,column=1,padx=15,pady=1)
entry5= Entry(frame,width=70)
entry5.grid(row=fila_grid,column=2,columnspan=2,padx=15,pady=1)
fila_grid+=1
#


#TLF.MOVIL
label9=Label(frame,text="Teléfono móvil:",anchor="w",width=40,background="gray",fg="white")
label9.grid(row=fila_grid,column=1,padx=15,pady=1)
entry6=Entry(frame,width=70)
entry6.grid(row=fila_grid,column=2,columnspan=2,padx=15,pady=1)
fila_grid+=1


#
#italic
#bold
#
boton1=Button(frame,text="Guardar",  width=21,command=guardar,font=("Verdana",10,"bold"))
boton1.grid(row=fila_grid,column=2,padx=1,pady=20)
boton2=Button(frame,text="Cancelar", width=21,command=exit,font=("Verdana",10,"bold"))
boton2.grid(row=fila_grid,column=3,padx=1,pady=20)

raiz.mainloop()