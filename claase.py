from tkinter import *
class principal():
    def _init__(self):
        self.ventana=Tk()
        self.ventana.title("Bienvenidos")
        self.ventana.config(bg="white")
        self.ventana.geometry("600x600")
    
        Menu_nuevo=Menu()
        actividad_menu=Menu(Menu_nuevo,tearoff=True)
        actividad_menu.add_command(label="Contador",command=self.Contador)
        actividad_menu.add_command(label="Resatdor",command=self.Restador)
        actividad_menu.add_command(label="Calculadora",command=self.Calculadora)
        actividad_menu.add_command(label="Lista",command=self.Lista)
        actividad_menu.add_command(label="Aleatorios")

        Menu_nuevo.add_cascada(menu=actividad_menu,label="Actividades")
        Menu_nuevo.add_cascada(label="Acerca de")
        Menu_nuevo.add_cascada(label="salir")

        self.ventana.config(menu=Menu_nuevo)
        self.ventana.mainloop()


    def Contador(self):
        pass
    def Restador(self):
        pass
    def Calculadora(self):
        pass
    def Lista(self):
        global num
        num=StringVar()

        def añadir():
            lista.insert(END,num.get())
            caja.delete(0,END)

        vent3=Toplevel()
        vent3.title("peliculas")
        vent3.config(bg="white")
        vent3.geometry("300x300")


        etiqueta=Label(vent3,text="pelicula")
        etiqueta.grid(row=1,column=0)

        caja=Entry(vent3)
        caja.grid(row=1,column=2)

        etiqueta2=Label(vent3,text="pelculas")
        etiqueta2.grid(row=2,column=1) 

        boton=Button(vent3,text="Añadir",command=añadir)
        boton.grid(row=4,column=4)

        lista=Listbox(vent3)
        lista.pack()



"""

    class eje1():

        def ContCreciente():
        
            ventana2=Toplevel()
            ventana2.title("Contador")
            ventana2.config(bg="white")
            ventana2.geometry("750x400")
        
            ventana2.mainloop()

            etiq1=Label(ventana2,text="Contador")
            etiq1.grid(row=1,column=0)

            caja1=Entry(ventana2,textvariale=num)
            caja1.grid(row=1,column=2)

            bot1=Button(ventana2,text="Sumar")
            bot1.grid(row=3,column=4)

      

        def sumar(self):
            self.numero.set(self.numero.get()+1)
        
        def reseteo(self):
            self.numero.set(0)

    class eje2():

        def ContDecreciente():
        
         ventana2=Toplevel()
         ventana2.title("Resta")
         ventana2.config(bg="white")
         ventana2.geometry("750x400")
    
         ventana2.mainloop()

         etiq1=Label(ventana2,text="Resta")
         etiq1.grid(row=1,column=0)

         caja1=Entry(ventana2,textvariale=num)
         caja1.grid(row=1,column=2)

        
         bot2=Button(ventana2,text="Restar")
         bot2.grid(row=4,column=4)

    
        def resta(self):
          self.numero.set(self.numero.get()-1)
        def reseteo(self):
          self.numero.set(0)
        
"""

app=principal()
