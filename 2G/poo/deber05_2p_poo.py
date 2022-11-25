from tkinter import *
from tkinter import messagebox

raiz=Tk()
raiz.title("Cajas de Texto")

frame=Frame(raiz,width=600)
frame.pack()


sub_total=StringVar()
cantidad =StringVar()

def calcular_entrys(event):
    #print("salio ")
    print("cantidad:",cantidad.get())
    print("precio unitario:",entry3.get())

    cant=0
    p_uni=0
    #validar que la caja de texto cantidad no este vacia
    if cantidad.get():
        #print("tiene valor")
        cant = float(cantidad.get())
    else:
        #print("no tiene nada")
        messagebox.showinfo("Cajas de Texto","Digite un valor para la cantidad, por favor!!")
        return False

    # validar que la caja de Precio unitario  no este vacia

    if entry3.get():
        #print("tiene valor")
        p_uni = float(entry3.get())
    else:
        #print("no tiene nada")
        messagebox.showinfo("Cajas de Texto","Digite el precio del producto por unidad, por favor!!")
        return False

    subt=cant*p_uni
    # print("subtotal:",subt)

    #subtotal = cantidad * precio unitario
    sub_total.set(str(subt))


def calcular_button():
    # print("salio ")
    print("cantidad:", cantidad.get())
    print("precio unitario:", entry3.get())

    cant = 0
    p_uni = 0
    # validar que la caja de texto cantidad no este vacia
    if cantidad.get() and entry3.get():
        # print("tiene valor")
        cant = float(cantidad.get())
        p_uni = float(entry3.get())

    else:
        # print("no tiene nada")
        messagebox.showinfo("Cajas de Texto", "Digite los valores, por favor!!")
        return False

    subt = cant * p_uni
    # print("subtotal:",subt)

    # subtotal = cantidad * precio unitario
    sub_total.set(str(subt))


label1=Label(frame,text="Items")
label1.grid(row=1,column=1,padx=10)
label2=Label(frame,text="Cantidad")
label2.grid(row=1,column=2,padx=10)
label3=Label(frame,text="Precio Unitario")
label3.grid(row=1,column=3,padx=10)
label4=Label(frame,text="Subtotal")
label4.grid(row=1,column=4,padx=10)

#items
entry1=Entry(frame,bg="yellow",fg="black")
entry1.grid(row=2,column=1,padx=10)

#cantidad
entry2=Entry(frame,bg="black",fg="white",textvariable=cantidad)
entry2.grid(row=2,column=2,padx=10)
entry2.bind("<Return>",calcular_entrys)

#precio unitario
entry3=Entry(frame,bg="cyan",fg="red",state="normal")
entry3.grid(row=2,column=3,padx=10)
entry3.bind("<Return>",calcular_entrys)

#subtotal
entry4=Entry(frame,bg="yellow",fg="black",
             textvariable=sub_total,
             state="disabled"
             #state="readonly"
               )
entry4.grid(row=2,column=4,padx=10)

#resultado
resultado=Button(frame,text="Calcular",command=calcular_button)
resultado.grid(row=2,column=0,padx=2)


#cantidad
entry2.insert(0,"0")

#precio unitario
entry3.insert(0,"0.00")

#subtotal
#insert funciona si state es normal
entry4.insert(0,"0.00")
sub_total.set("0.00")

raiz.mainloop()
