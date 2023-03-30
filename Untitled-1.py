from tkinter import*

def principal():
    global ventana
    ventana=Tk()
    ventana.config('200x300')
    ventana.title('hola')
    ventana.resizable(width=True,height=False)
    menu=Menu(ventana)
    ventana.config(menu=menu)

    menu.add_cascade(Label,'holapai')