
from cProfile import label
from tkinter import *

class principal():
    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Bienvenidos")
        self.ventana.config(bg="white")
        self.ventana.geometry("600x600")

        barra_menu = Menu()
        menu_admin = Menu(barra_menu, tearoff=False)
        menu_com = Menu(barra_menu, tearoff=False)
        #menu_ganan = Menu(barra_menu, tearoff=False)
        #menu_salida = Menu(barra_menu, tearoff=False)

        menu_com.add_command(label="alta",command=self.alta)
        menu_com.add_command(label="Baja",command=self.baja)
        barra_menu.add_cascade(menu=menu_com,label="Admin Abon",command=self.admin) 

        menu_admin.add_command(label="ingreso")
        barra_menu.add_cascade(label="ingreso",command=self.inicioSesion)

        menu_admin.add_command(label="ganancias")
        barra_menu.add_cascade(label="ganancias",command=self.ganancias)


        barra_menu.add_cascade(label="Acerca de",command=self.acercade) 
        barra_menu.add_cascade(label="Salir",command=self.ventana.destroy)

        self.ventana.config(menu=barra_menu)
        self.ventana.mainloop()

        foto=PhotoImage(file="pngegg.png").subsample(3)
        imagen_etiqueta=Label(self.ventana,image=foto)
        imagen_etiqueta.pack()
        self.ventana.mainloop()

        


      
    def inicioSesion(self): 
        nom=StringVar()
        contra=StringVar()
        nom2=StringVar()
        contra2=StringVar()
    
        raiz2=Toplevel()
        raiz2.title("Iniciar Sesion")
        raiz2.config(bg="white")
        raiz2.geometry("750x400")
    

        etiq=Label(raiz2,text="Usuario")
        etiq.grid(column=0,row=0)

        etiq2=Label(raiz2,text="Contraseña")
        etiq2.grid(column=0,row=1)

        def inicio():
            if nom2.get()!="" and contra2.get()!="":
                if nom.get()==nom2.get() and contra.get()==contra2.get():
                 ac=Label(raiz2,text="Acceso concedido",fg="Green")
                 ac.place(x=60,y=100)
                else:
                 ac=Label(raiz2,text="Acceso Denegado",fg="red")
                 ac.place(x=60,y=100)
            else:
                    ac=Label(raiz2,text="Usiario No Registrado")
                    ac.place(x=60,y=100)


        caj=Entry(raiz2,textvariable=nom)
        caj.place(x=90,y=4)

        caj2=Entry(raiz2,textvariable=contra)
        caj2.place(x=90,y=25)

        bott=Button(raiz2,text="Entrar",command=inicio)
        bott.place(x=50,y=50)
 
        bott2=Button(raiz2,text="Salir",command=raiz2.destroy)
        bott2.place(x=100,y=50)

        '''foto=PhotoImage(file="pngegg.png")
        imagen_etiqueta=Label(raiz2,image=foto)
        imagen_etiqueta.pack()'''
        self.ventana.mainloop()


    def admin(self):
        lost=Toplevel()
        lost.title("admin de abon")
        lost.config(bg="white")
        lost.geometry("750x400")

        cajita=Entry(lost)
        cajita.grid(column=5,row=0)
        etiqA=Label(lost,text="Nombre De Usuario")
        etiqA.grid(column=3,row=0)

        cajita=Entry(lost)
        cajita.grid(column=5,row=1)
        etiqA=Label(lost,text="DNI")
        etiqA.grid(column=3,row=1)

    def alta(self):
        cass=Toplevel()
        cass.title("admin de abon")
        cass.config(bg="blue")
        cass.geometry("300x300")


        etiqA=Label(cass,text="DNI")
        etiqA.grid(column=1,row=0)
        cajitaA=Entry(cass)
        cajitaA.grid(column=2,row=0)

        etiqB=Label(cass,text="Nombre")
        etiqB.grid(column=1,row=1)
        cajitaB=Entry(cass)
        cajitaB.grid(column=2,row=1)

        etiqC=Label(cass,text="Apellido")
        etiqC.grid(column=1,row=2)
        cajitaC=Entry(cass)
        cajitaC.grid(column=2,row=2)

        etiqD=Label(cass,text="Tipo de veh")
        etiqD.grid(column=1,row=3)
        cajitaD=Entry(cass)
        cajitaD.grid(column=2,row=3)

        etiqE=Label(cass,text="Patente")
        etiqE.grid(column=1,row=4)
        cajitaE=Entry(cass)
        cajitaE.grid(column=2,row=4)

        etiqF=Label(cass,text="Marca")
        etiqF.grid(column=1,row=5)
        cajitaF=Entry(cass)
        cajitaF.grid(column=2,row=5)

        etiqG=Label(cass,text="Modelo")
        etiqG.grid(column=1,row=6)
        cajitaG=Entry(cass)
        cajitaG.grid(column=2,row=6)

        bott3=Button(cass,text="Guardar",command=cass.destroy)
        bott3.place(x=50,y=150)
    

    def baja(self):
        chos=Toplevel()
        chos.title("admin de abon")
        chos.config(bg="black")
        chos.geometry("300x300")

        E=Label(chos,text="DNI")
        E.grid(column=1,row=0)
        c=Entry(chos)
        c.grid(column=2,row=0)

        E1=Label(chos,text="Nombre")
        E1.grid(column=1,row=1)
        c1=Entry(chos)
        c1.grid(column=2,row=1)

        E1=Label(chos,text="Apellido")
        E1.grid(column=1,row=2)
        c1=Entry(chos)
        c1.grid(column=2,row=2)

        

        bott=Button(chos,text="Modificar",command=chos.destroy)
        bott.grid(column=2,row=3)

        bott=Button(chos,text="Eliminar",command=chos.destroy)
        bott.grid(column=3,row=3)


        botk=Button(chos,text="Buscar",command=chos.destroy)
        botk.grid(column=7,row=1)

        P=Label(chos,text="Patente")
        P.grid(column=1,row=15)
        K=Entry(chos)
        K.grid(column=2,row=15)

        botk=Button(chos,text="Buscar",command=chos.destroy)
        botk.grid(column=7,row=15)

        K=Entry(chos)
        K.grid(column=2,row=18)

        K=Entry(chos)
        K.grid(column=2,row=19)

        bott=Button(chos,text="Modificar",command=chos.destroy)
        bott.grid(column=2,row=20)

        bott=Button(chos,text="Eliminar",command=chos.destroy)
        bott.grid(column=3,row=20)

    def ganancias(self):
        top=Toplevel()
        top.title("admin de abon")
        top.config(bg="white")
        top.geometry("300x300")

        EL=Label(top,text="ganancias del dia")
        EL.grid(column=1,row=1)

        EL=Label(top,text="CANT VEH")
        EL.grid(column=1,row=2)

        EL=Label(top,text="CANT MOTOS")
        EL.grid(column=1,row=3)


    def acercade(self):
        mi=Toplevel()
        mi.title("acerca de")
        mi.config(bg="gray")
        mi.geometry("200x200")
        
        las=Label(mi,text="Debora Muscarello")
        las.grid(column=3,row=0)
        las2=Label(mi,text="Programacion 3")
        las2.grid(column=3,row=1)





principal()
