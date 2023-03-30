from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.title("treeview")
ventana.geometry("800x600")
ventana.config(bg="Sky blue")

nomb=StringVar()
apell=StringVar()
direc=StringVar()

nom=Label(ventana,text="nombre").grid(row=0,column=0)
caj=Entry(ventana,textvariable=nomb).grid(row=0,column=1)
ape=Label(ventana,text="apellido").grid(row=1,column=0)
caj1=Entry(ventana,textvariable=apell).grid(row=1,column=1)

dire=Label(ventana,text="direcion").grid(row=2,column=0)
Entry(ventana,textvariable=direc).grid(row=2,column=1)





    
def guardar():
    tabla.insert("",END,text=nomb.get(),values=(apell.get(),direc.get()))
    nomb.set("")
    apell.set("")
    direc.set("")

    



ttk.Button(ventana,text="save",command=guardar).grid(row=3,column=2)


tabla=ttk.Treeview(ventana,columns=(1,2))
tabla.place(x=150,y=200)
tabla.heading("#0",text="NOMBRE",anchor=CENTER)
tabla.heading("1",text="APELLIDO",anchor=CENTER)
tabla.heading("2",text="DIRECCION",anchor=CENTER)








 
ventana.mainloop()