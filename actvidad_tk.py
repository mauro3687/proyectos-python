from tkinter import*
raiz= Tk()
raiz.title("saludo")
raiz.geometry("740x400")
nombre=Label(raiz,text='Nombre')
nombre.grid()
apellido=Label(raiz,text='Apellido')
apellido.grid()

nom= StringVar()
ape=StringVar()

nombre=Entry(raiz,textvariable=nom,width=20)
nombre.grid(row=0,column=2)
nombre.focus()

apellido=Entry(raiz,textvariable=ape,width=20)
apellido.grid(row=1,column=2)
apellido.focus()

def saludar():
    buenas=Label(raiz,text=('hola,',nombre.get(),apellido.get()))
    buenas.grid(row=5,column=2)
#botones
boton=Button(raiz,text="saludar",command=saludar)
boton.grid()

foto=Photolimage(file='')



    
               
    
    




