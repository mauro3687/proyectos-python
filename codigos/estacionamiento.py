from cProfile import label
from cgitb import text
from sqlite3 import Row
from tkinter import *
from tkinter import messagebox
from tkinter.tix import COLUMN
root=Tk()
root.title("Estacionamiento Universidad")
root.iconbitmap("imagenes\estaico.ico")
root.geometry("1315x690")
root.resizable(0,0)


class Estacionamiento():
    
    def salirApp():
        
        Salir=messagebox.askokcancel("Atencion","¿Desea salir de la aplicacion?")
       
        if Salir==True:
            root.destroy()
    
    def infoVersion():
        
        Version=messagebox.showinfo("Vercion","Vercion: 1.0.0 - Build: C0B0I0")


    def acercaDe():
        
        acercaDe=messagebox.showinfo("Estacionamiento Universidad","Creado por: \nAlejo Labasto \nCopyrigth © 2022")



    def abono():
        ventana_abono=Toplevel()
        ventana_abono.iconbitmap("imagenes\estaico.ico")
        ventana_abono.config(bg="#55ddbd")
        ventana_abono.resizable(0,0)
        #________cuadros de txt______
        cuadroDNI=Entry(ventana_abono)
        cuadroDNI.grid(row=0,column=1)
        cuadroDNI.config(fg="black",justify="left")

        cuadroNombre=Entry(ventana_abono)
        cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
        cuadroNombre.config(fg="black",justify="left")

        cuadroApellido=Entry(ventana_abono)
        cuadroApellido.grid(row=2,column=1,padx=10,pady=10)
        cuadroApellido.config(fg="black" ,justify="left")
        
        cuadroTipo=Entry(ventana_abono)
        cuadroTipo.grid(row=4,column=1,padx=10,pady=10)
        cuadroTipo.config(fg="black",justify="left")


        cuadroPatente=Entry(ventana_abono)
        cuadroPatente.grid(row=3,column=1,padx=10,pady=10)
        cuadroPatente.config(fg="black",justify="left")

        cuadroMarca=Entry(ventana_abono)
        cuadroMarca.grid(row=5,column=1,padx=10,pady=10)
        cuadroMarca.config(fg="black",justify="left")

        cuadroModelo=Entry(ventana_abono)
        cuadroModelo.grid(row=6,column=1,padx=10,pady=10)
        cuadroModelo.config(fg="black",justify="left")


        DNIlabel=Label(ventana_abono,text="DNI")
        DNIlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

        Nombrelabel=Label(ventana_abono,text="Nombre")
        Nombrelabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

        Apellidolabel=Label(ventana_abono,text="Apellido")
        Apellidolabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

        Tipolabel=Label(ventana_abono,text="Tipo veiculo")
        Tipolabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

        Patentelabel=Label(ventana_abono,text="Pantente")
        Patentelabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

        Marcalabel=Label(ventana_abono,text="Marca")
        Marcalabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

        Modelolabel=Label(ventana_abono,text="Modelo")
        Modelolabel.grid(row=6,column=0,sticky="e",padx=10,pady=10)

        botonGuardar=Button(ventana_abono, text="Guardar")
        botonGuardar.grid(row=7,column=1,sticky="e",pady=10, padx=10)
    #________________________________________________________________________________________________________
    # ______________________________________________________________________________________________________              
    def baja_mod():
        ventana_baja_mod=Toplevel()
        ventana_baja_mod.iconbitmap("imagenes\estaico.ico")
        ventana_baja_mod.config(bg="#00a1f6")
        ventana_baja_mod.resizable(0,0)
        #________cuadros de txt______
        cuadroDNI=Entry(ventana_baja_mod)
        cuadroDNI.grid(row=0,column=1)
        cuadroDNI.config(fg="black",justify="left")

        cuadroNombre=Entry(ventana_baja_mod)
        cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
        cuadroNombre.config(fg="black",justify="left")

        cuadroApellido=Entry(ventana_baja_mod)
        cuadroApellido.grid(row=2,column=1,padx=10,pady=10)
        cuadroApellido.config(fg="black" ,justify="left")
        
        botonEliminar=Button(ventana_baja_mod, text="Eliminar")
        botonEliminar.grid(row=3,column=1,sticky="e",pady=10, padx=10)

        botonMod=Button(ventana_baja_mod, text="Modificar")
        botonMod.grid(row=3,column=0,sticky="e",pady=10, padx=10)

        cuadroTipo=Entry(ventana_baja_mod)
        cuadroTipo.grid(row=4,column=1,padx=10,pady=10)
        cuadroTipo.config(fg="black",justify="left")


        cuadroPatente=Entry(ventana_baja_mod)
        cuadroPatente.grid(row=5,column=1,padx=10,pady=10)
        cuadroPatente.config(fg="black",justify="left")

        cuadroMarca=Entry(ventana_baja_mod)
        cuadroMarca.grid(row=6,column=1,padx=10,pady=10)
        cuadroMarca.config(fg="black",justify="left")

        cuadroModelo=Entry(ventana_baja_mod)
        cuadroModelo.grid(row=7,column=1,padx=10,pady=10)
        cuadroModelo.config(fg="black",justify="left")


        DNIlabel=Label(ventana_baja_mod,text="DNI")
        DNIlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

        Nombrelabel=Label(ventana_baja_mod,text="Nombre")
        Nombrelabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

        Apellidolabel=Label(ventana_baja_mod,text="Apellido")
        Apellidolabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

        Tipolabel=Label(ventana_baja_mod,text="Tipo veiculo")
        Tipolabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

        Patentelabel=Label(ventana_baja_mod,text="Pantente")
        Patentelabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

        Marcalabel=Label(ventana_baja_mod,text="Marca")
        Marcalabel.grid(row=6,column=0,sticky="e",padx=10,pady=10)

        Modelolabel=Label(ventana_baja_mod,text="Modelo")
        Modelolabel.grid(row=7,column=0,sticky="e",padx=10,pady=10)

        botonEliminar1=Button(ventana_baja_mod, text="eliminar")
        botonEliminar1.grid(row=8,column=1,sticky="e",pady=10, padx=10)

        botonMod1=Button(ventana_baja_mod, text="Modificar")
        botonMod1.grid(row=8,column=0,sticky="e",pady=10, padx=10)

    def saldo():
        ventana_saldo=Toplevel()
        ventana_saldo.iconbitmap("imagenes\estaico.ico")
        ventana_saldo.config(bg="#5a2fd0")
        ventana_saldo.resizable(0,0)

        cuadroDNI=Entry(ventana_saldo)
        cuadroDNI.grid(row=0,column=1)
        cuadroDNI.config(fg="black",justify="left")   
        
        cuadroSaldo=Entry(ventana_saldo)
        cuadroSaldo.grid(row=1,column=1)
        cuadroSaldo.config(fg="black",justify="left") 

        DNIlabel=Label(ventana_saldo,text="DNI")
        DNIlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)
        
        Saldolabel=Label(ventana_saldo,text="saldo")
        Saldolabel.grid(row=1,column=0,sticky="e",padx=10,pady=10) 
        def saldoFinal():
            messagebox.showinfo("SALDO","Su saldo ahora es:\n")

        def SaldoFav():
            messagebox.showinfo("SALDO","Su saldo es:")
            

        botonCobr=Button(ventana_saldo, text="cobrar",command=saldoFinal)
        botonCobr.grid(row=3,column=0,sticky="e",pady=10, padx=10)

        botonSaldoFav=Button(ventana_saldo, text="saldo a favor",command=SaldoFav)
        botonSaldoFav.grid(row=3,column=1,sticky="e",pady=10, padx=10)



    barraMenu=Menu(root)
    root.config(menu=barraMenu, width=300, height=300)
    
    adminMenu=Menu(barraMenu, tearoff=0)
    adminMenu.add_command(label="Administracion")
    adminMenu.add_separator()
    adminMenu.add_command(label="Salir",command=salirApp)

    AbonadoMenu=Menu(barraMenu, tearoff=0)
    AbonadoMenu.add_command(label="Abonado/Alta",command=abono)

    BajaModMenu=Menu(barraMenu, tearoff=0)
    BajaModMenu.add_command(label="Baja/Mod",command=baja_mod) 
    
    SaldoMenu=Menu(barraMenu, tearoff=0)
    SaldoMenu.add_command(label="Saldo",command=saldo)

    AyudaMenu=Menu(barraMenu, tearoff=0)
    AyudaMenu.add_command(label="Version",command=infoVersion)
    AyudaMenu.add_command(label="Novedades")
    AyudaMenu.add_command(label="Acerca de...",command=acercaDe)


    barraMenu.add_cascade(label="Avanzado", menu=adminMenu)
    barraMenu.add_cascade(label="Abonado/alta", menu=AbonadoMenu)
    barraMenu.add_cascade(label="Baja/Mod", menu=BajaModMenu)    
    barraMenu.add_cascade(label="Saldo", menu=SaldoMenu) 
    barraMenu.add_cascade(label="Ayuda",menu=AyudaMenu)

    
    
    def login():
        miFrameLogin=Toplevel()
        miFrameLogin.title("Estacionamiento Universidad - Acceso")
        miFrameLogin.iconbitmap("imagenes\estaico.ico")
        miFrameLogin.resizable(0,0)
        miFrameLogin.geometry("+500+250")
        miFrameLogin.config(bg="#1F1F1F")
        miFrameLogin2=Frame(miFrameLogin)
        miFrameLogin2.pack(fill="both", expand="True")
        miFrameLogin2.config(bg="#1F1F1F")
        miFrameLogin2.config(width=1200, height=600)
        miFrameLogin2.config(bd=15)
        miFrameLogin2.config(relief="groove")

        def verificar():
            if  miCuadroUsuario.get().upper()=="USER" and miCuadroClave.get().upper()=="1234":
                messagebox.showinfo(title="login correcto", message="Bienvenido" + miCuadroUsuario.get())
                miFrameLogin.destroy()
                root.iconify()    
                root.deiconify()
            else:
                messagebox.showerror(title="Login incorrecta", message="usuario o contraseña icorrecta")

        def salirLogin():
            root.destroy()

    
        miCuadroUsuario=StringVar()
        miCuadroClave=StringVar()

        labelUsuario=Label( miFrameLogin2, text="USUARIO: ", bg="#1F1F1F", fg="#03f943")
        labelUsuario.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        cuadroUsuario=Entry(miFrameLogin2, textvariable=miCuadroUsuario)
        cuadroUsuario.grid(row=0, column=1, padx=10, pady=10)
        lableClave=Label( miFrameLogin2, text="CLAVE", bg="#1F1F1F", fg="#03f943")
        lableClave.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        cuadroClave=Entry(miFrameLogin2, show="*", textvariable=miCuadroClave)
        cuadroClave.grid(row=1, column=1, padx=10, pady=10)
        botonEntrar=Button(miFrameLogin2, text="Entrar", width=10,height=1, borderwidth=1,highlightbackground="#1F1F1F", command=verificar)
        botonEntrar.grid(row=2, column=0,columnspan=3, padx=10, pady=10)
    
        cuadroClave.bind('<Return>',lambda x: verificar())
        miFrameLogin.protocol("WM_DELETE_WINDOW",salirLogin)
        miFrameLogin.mainloop()



    miFrame=Frame(root)
    miFrame.pack(fill="both", expand="True")
    miFrame.config(bg="#1F1F1F")
    miFrame.config(width="1280", height="920")
    miFrame.config(bd=15)
    miFrame.config(relief="groove")

    
    imagenFondo=PhotoImage(file="imagenes\esta2.5.png")
    Label(miFrame, image=imagenFondo, bg="#1F1F1F").place(x=0, y=0)
    imagenTitulo=PhotoImage(file="imagenes\Estacionamiento-Universi.png")
    Label(miFrame, image=imagenTitulo, bg="#1F1F1F").place(x=288, y=0)
    
    root.withdraw()
    login()












root.mainloop()
