from tkinter import *

raiz = Tk()
raiz.title("Formulario de clientes")
raiz.iconbitmap("banco.ico")
frame=Frame(raiz,width=500, height=600)
frame.pack()

Label(frame,text="Digite Nombres: ",fg="red").  place(x=50,y=50)
Label(frame,text="Digite Apellidos: ",fg="red").place(x=50,y=80)
Label(frame,text="Digite Nacionalidad: ",fg="red").place(x=50,y=110)
Label(frame,text="Digite Dirección de residencia: ",fg="red").place(x=50,y=140)
Label(frame,text="Digite Dirección del lugar de trabajo: ",fg="red").place(x=50,y=170)
Label(frame,text="Digite Cédula: ",fg="red").place(x=50,y=200)
Label(frame,text="Digite Correo: ",fg="red").place(x=50,y=230)
Label(frame,text="Digite Fecha de nacimiento: ",fg="red").place(x=50,y=260)
Label(frame,text="Digite Teléfono móvil: ",fg="red").place(x=50,y=290)
Label(frame,text="Digite Teléfono convencional de casa: ",fg="red").place(x=50,y=320)
Label(frame,text="Digite Teléfono del trabajo: ",fg="red").place(x=50,y=350)
Label(frame,text="Digite Teléfono de contacto 1: ",fg="red").place(x=50,y=380)
Label(frame,text="Digite Teléfono de contacto 2: ",fg="red").place(x=50,y=410)
Label(frame,text="Digite Teléfono decontacto 3: ",fg="red").place(x=50,y=440)
Label(frame,text="Digite Contacto 1: ",fg="red").place(x=50,y=470)
Label(frame,text="Digite Contacto 2: ",fg="red").place(x=50,y=500)
Label(frame,text="Digite Contacto 3: ",fg="red").place(x=50,y=530)
Label(frame,text="Digite Genero: ",fg="red").place(x=50,y=560)

# para cajas de texto usamos este objeto entry
#lo mismo con place le ubicamos coordenadas x para las columnas y y para filas
Entry(frame).place(x=280,y=50)
Entry(frame).place(x=280,y=80)
Entry(frame).place(x=280,y=110)
Entry(frame).place(x=280,y=140)
Entry(frame).place(x=280,y=170)
Entry(frame).place(x=280,y=200)
Entry(frame).place(x=280,y=230)
Entry(frame).place(x=280,y=260)
Entry(frame).place(x=280,y=290)
Entry(frame).place(x=280,y=320)
Entry(frame).place(x=280,y=350)
Entry(frame).place(x=280,y=380)
Entry(frame).place(x=280,y=410)
Entry(frame).place(x=280,y=440)
Entry(frame).place(x=280,y=470)
Entry(frame).place(x=280,y=500)
Entry(frame).place(x=280,y=530)
Entry(frame).place(x=280,y=560)

#nombres=input("digite nombres ")

raiz.mainloop()















