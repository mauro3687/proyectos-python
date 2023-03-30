from cProfile import label
from calendar import c
from cgitb import text
from distutils.cmd import Command
from operator import contains
from sqlite3 import Row
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import tkinter.messagebox
import random







def menu():
    global pantalla
    pantalla =Tk()
    pantalla.geometry('150x150')
    pantalla.title('Login')
    pantalla.resizable(width=True,height=False)
    menu=Menu(pantalla)
    pantalla.config(menu=menu)

    CC= Menu(menu, tearoff=0)
    CD=Menu(menu,tearoff=0)
    R=Menu(menu,tearoff=0)
    INI=Menu(menu,tearoff=0)
    Ge=Menu(menu,tearoff=0)

    
    menu.add_cascade(label='ContCreciente',command=ContCreci)
    menu.add_cascade(label='ContDecreciente',command=ContDecreciente)
    menu.add_cascade(label='Registro',command=registro)
    menu.add_cascade(label='Inicio sesion',command=inicio)
    menu.add_cascade(label='Generador_num',command=aleatorio)
  


    pantalla.mainloop()
    

def inicio ():
    global pantalla1
    pantalla1=Toplevel(pantalla)
    pantalla1.geometry('300x150')
    pantalla1.title('Ingreso de usuario')
    Usua=Label(pantalla1,text="usuario")
    Usua.config(font=('Ravie',12,'underline'))
    Usua.grid() 
    usu=StringVar()
    usuario=Entry(pantalla1,textvariable=usu,width=20)
    usuario.grid()
    cont=Label(pantalla1,text="Contraseña")
    cont.config(font=('Ravie',12,'underline'))
    cont.grid()
    contra=StringVar()
    contraseña=Entry(pantalla1,textvariable=contra,show="*")
    contraseña.grid()
    entra=Button(pantalla1,text="Entrar")
    entra.grid(row=5,column=0)

    salir=Button(pantalla1,text="Salir",command=pantalla1.destroy)
    salir.grid(row=5,column=1)
    usa=usuario.get()
    cont=contraseña.get()
    if usa=="eze" and cont=="1234":
        correcta()
   



def correcta():
    global pantalla1_5
    pantalla1_5= Toplevel()











def registro ():
    global pantalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry('300x150')
    pantalla2.title('Registrate')
    Usua=Label(pantalla2,text="usuario")
    Usua.config(font=('Ravie',12,'underline'))
    Usua.grid()
    
    usu=StringVar()
    usuario=Entry(pantalla2,textvariable=usu,width=20)
    usuario.grid()
    cont=Label(pantalla2,text="Contraseña")
    cont.config(font=('Ravie',12,'underline'))
    cont.grid()
    contra=StringVar()
    contraseña=Entry(pantalla2,textvariable=contra,show="*")
    contraseña.grid()

    regist=Button(pantalla2,text="Registar")
    regist.grid(row=5,column=0)
    

def ContCreci():
    global pantalla3
    global num
    pantalla3 =Toplevel(pantalla)
    pantalla3.geometry('300x150')
    
    
    
    num=IntVar()
    numero=Entry(pantalla3,textvariable=num,state='disabled')
    numero.grid(row=0,column=1)

    con=Button(pantalla3,text="+",command=sumar)
    con.grid(row=0,column=3)
    
def sumar():
    num.set(num.get()+1)
    

def peliculas():
    global raiz
    raiz =Toplevel(pantalla)
    raiz.geometry('300x150')
    
    buscador=StringVar()
    buscador_pelis=Entry(raiz,textvariable=buscador)
    buscador_pelis.pack()
    caja=Listbox(raiz)
    caja.pack()
    def agregar():
        caja.insert(0,buscador.get())
    boton_reset=Button(raiz,text="Añadir",command=agregar)
    boton_reset.pack()

#----------------------------------------------------



def ContDecreciente():
    global pantalla4
    global num1
    pantalla4 =Toplevel(pantalla)
    pantalla4.geometry('300x150')

    
    cont=Button(pantalla4,text="-",command=restar)
    cont.grid(row=0,column=5)
    vol=Button(pantalla4,text="Volver",command=pantalla4.destroy)
    vol.grid(row=4,column=24)

    num1=IntVar()
    numero1=Entry(pantalla4,text="88",textvariable=num1,state='disabled')
    numero1.grid(row=0,column=1)



def restar():

    num1.set(num1.get()-1)



def aleatorio():
    global raiz1
    raiz1=Toplevel(pantalla)
    raiz1.geometry("400x300")
    global a
    global b
    global c
    a=IntVar()
    b=IntVar()
    c=IntVar()
    prim=Entry(raiz1,textvariable=a)
    prim.grid(row=1, column=2)
    segund=Entry(raiz1,textvariable=b)
    segund.grid(row=2, column=2)
    resul=Entry(raiz1,textvariable=c,state='disabled')
    resul.grid(row=3, column=2)
    num_m=Label(raiz1,text="numero 1")
    num_m.grid(row=1, column=1)
    num=Label(raiz1,text="numero 2")
    num.grid(row=2, column=1)
    num_g=Label(raiz1,text="Resultado")
    num_g.grid(row=3, column=1)

    generar_boton=Button(raiz1,text="Generar",command=generar)
    generar_boton.grid(row=4,column=4)

def generar():
    i=random.randint(a.get(), b.get())
    c.set(i)
       
"""def GeneradorA():
    global raiz
    global pantalla4_5
    pantalla4_5=Toplevel(pantalla)
    pantalla4_5.geometry('750x300')
    pantalla4_5.title('GENERADOR DE NUMEROS ALEATORIOS')
    n1=Label(pantalla4_5,text="Numero_1")
    n2=Label(pantalla4_5,text="Numero_2")
    nRandom=Label(pantalla4_5,text="Numero Generado  ")
    n1.grid(row=2,column=6)
    print("")
    n2.grid(row=4,column=6)
    print("")
    nRandom.grid(row=6,column=6)
    cj_1=StringVar()
    caja=Entry(pantalla4_5,textvariable=cj_1,width=20)
    caja.grid(row=6,column=8)
    
    
    opc= ["1","2","3","4","5","6","7",
    "8","9","10","11","12","13",
    "14","15","16","17","18","19","20"] 
    combo=ttk.Combobox(pantalla4_5,width=15,values=opc,state="readonly")
    combo.grid(row=2,column=8)

    opc1= ["1","2","3","4","5","6","7",
    "8","9","10","11","12","13",
    "14","15","16","17","18","19","20"] 
    combo1=ttk.Combobox(pantalla4_5,width=15,values=opc1,state="readonly")
    combo1.grid(row=4,column=8)
    Gene=Button(pantalla4_5,text="Genera")
    Gene.grid(row=8,column=8)
    vol=Button(pantalla4_5,text="Volver",command=pantalla4_5.destroy)
    vol.grid(row=8,column=6)
    n=random.randint(1, 20)"""
    

    










    





  






   






  


        
    
    


    
    
   
        
        

menu()
















































    



