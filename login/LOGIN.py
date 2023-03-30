from tkinter import*
from tkinter import messagebox


def login ():
    global raiz
    global caja1
    global caja2
    raiz=Tk()
    raiz.geometry("600x400")
    raiz.config(bg="#5F9EA0")
    raiz.title("login del empleado")
    raiz.iconbitmap("cslogin_94432.ico")
    caja1=StringVar()
    caja2=StringVar()
    

    imagen=PhotoImage(file='LOGIN.png')
    image_frame=Label(raiz,image=imagen).place(x=105,y=0)


    ENO=Label(raiz,text="nombre del empleado").place(x=230,y=200)
    caj=Entry(raiz,textvariable=caja1,width=20).place(x=230,y=230)

    Eco=Label(raiz,text="contraseña").place(x=230,y=260)
    caj2=Entry(raiz,textvariable=caja2,width=20,show="*").place(x=230,y=290)

    boto=Button(raiz,text="INGRESAR",command=regista).place(x=200,y=320)

    boto1=Button(raiz,text="REGISTAR",command=registro).place(x=280,y=320)

  
    raiz.mainloop()




def registro():
    global raiz1
    global cont
    global nom
    raiz1=Toplevel(raiz)
    raiz1.geometry("600x400")
    raiz1.config(bg="#5F9EA0")
    raiz1.title("REGISTRO DEL EMPLEADO")
    raiz1.iconbitmap("cslogin_94432.ico")
    nom=StringVar()
    cont=StringVar()
   

    imagen=PhotoImage(file='LOGIN.png')
    image_frame=Label(raiz1,image=imagen).place(x=105,y=0)


    ENO=Label(raiz1,text="nombre del empleado").place(x=230,y=200)
    caj=Entry(raiz1,textvariable=nom,width=20).place(x=230,y=230)
    Eco=Label(raiz1,text="contraseña").place(x=230,y=260)
    caj2=Entry(raiz1,textvariable=cont,width=20,show="*").place(x=230,y=290)

    boto=Button(raiz1,text="REGISTAR",command=guardar).place(x=260,y=320)
    
def regista():
    if nom.get()=="" and caja2.get()=="":
        messagebox.showinfo("No Registrado","Usted No Esta Registrado")
    
    elif nom.get() == caja1.get() and cont.get() == caja2.get():
        
        messagebox.showinfo("Completado","Inicio De Sesion Completado")
    
    elif caja1() != nom.get() and caja2.get() != cont.get():
        messagebox.showinfo("Error","Usuario O Contraseña Incorrecta")


def guardar():
    messagebox.showinfo("Completado","Registro Completado")

    

login()