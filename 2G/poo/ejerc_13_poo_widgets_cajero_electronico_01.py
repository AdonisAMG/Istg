from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

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
        presentar = f"nombres: {self.nombres}\nnacionalidad:{self.nacionalidad}\ndireccion:{self.direccion}\ncedula:{self.cedula}\ncorreo:{self.correo}\nfecha de nac.:{self.fecha_nac}\ntlf_movil:{self.tlf_movil}\ntlf_conv:{self.tlf_conv}\ntlf_contacto:{self.tlf_contacto}\ncontacto:{self.contacto}"
        return presentar




def guardar():
    messagebox.showinfo("Formulario Clientes","Cliente Guardado con Exito")


    #obtener info de un entry en este caso del entry de nombres
    nombres=entry1.get()
    print("nombres ",nombres)

    #apellido = input("digite apellidos")
    apellido = entry2.get()
    #capturar los otros entrys restantes

    #crear una instancia de la clase cliente
    c=Cliente()
    #invocar al metodo crear_cliente y pasar los argumentos
    #c.crear_cliente(nombres,,)
    #imprimir el objeto deseado
    print(c)




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
entry5=Entry(frame,width=70)
entry5.grid(row=fila_grid,column=2,columnspan=2,padx=15,pady=1)
fila_grid+=1
#
# #CORREO
label7=Label(frame,text="Correo:",anchor="w",width=40,background="gray",fg="white")
label7.grid(row=fila_grid,column=1,padx=15,pady=1)
entry6= Entry(frame,width=70)
entry6.grid(row=fila_grid,column=2,columnspan=2,padx=15,pady=1)
fila_grid+=1
#


#TLF.MOVIL
label9=Label(frame,text="Teléfono móvil:",anchor="w",width=40,background="gray",fg="white")
label9.grid(row=fila_grid,column=1,padx=15,pady=1)
entry8=Entry(frame,width=70)
entry8.grid(row=fila_grid,column=2,columnspan=2,padx=15,pady=1)
fila_grid+=1


#
#italic
#bold
#
boton1=Button(frame,text="Guardar",  width=21,command=guardar,font=("Verdana",10,"bold"))
boton1.grid(row=fila_grid,column=2,padx=1,pady=20)
boton2=Button(frame,text="Cancelar", width=21,command=guardar,font=("Verdana",10,"bold"))
boton2.grid(row=fila_grid,column=3,padx=1,pady=20)

raiz.mainloop()
