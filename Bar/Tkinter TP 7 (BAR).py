from tkinter import*
from tkinter import messagebox, ttk, Button, PhotoImage
from pickle import*
import os
from os import path
import tkinter.font as tkFont

"""----------Ventana Principal-----------"""

ventana=Tk()
ventana.title("Bar El Cortadito")
ventana.resizable(width=False,height=False)
ventana.config(bg="#d8e3f8")
ventana.config(width="1280",height="720")
ventana.iconbitmap("0001.ico")

#BOTONES = PEDIDOS, CLIENTES Y PERSONAL

""""------------------FRAME----------------"""

mi_frame = Frame(ventana)
mi_frame.place(x=0,y=0)
mi_frame.config(width="190",height="1500")
mi_frame.config(bg="#03bb85")

#Botonoes    

pedi=Button(mi_frame,text="Logeo").place(x=100,y=100)
pedi=Button(mi_frame,text="Pedidos",command=pedi).place(x=100,y=200)
pedi=Button(mi_frame,text="Administracion").place(x=50,y=300)

"""----------------MENU------------------"""
#----------------------login---------------------
#-----------------pedido---------------------
"""def pedi():
    global ventana1
    ventana1=Toplevel(ventana)
    ventana1.title("PEDIDOS")    
    ventana1.config("990x710")
    ventana1.iconbitmap("0001.ico")"""

#-----------------------------------------------------

def salir():
    ventana.destroy()

def MV():
    ventana.attributes('-fullscreen',False)

#-----------------------------------------------------

def info():
    messagebox.showinfo("Creadores","Creadores: Labasto,Gorosito Y Videla \n ©Ipet 57 Programacion")

#-----------------------------------------------------

barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

archivo = Menu(barra_menu,tearoff=0)

barra_menu.add_cascade(label='Menu',menu=archivo)
archivo.add_separator()
archivo.add_command(label='Salir',command=salir)
archivo.add_command(label='MV',command=MV)

pantalla1 = Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label='Info',menu=pantalla1)
pantalla1.add_command(label='Creador',command=info)
