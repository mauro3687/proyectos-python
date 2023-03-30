from tkinter import * 
from tkinter import messagebox 
import sqlite3

# -------------FUNCIONES------------------------------------
def conexionBBDD(): #función para crear bbdd con el menú
    miConexion=sqlite3.connect("ventas")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
           CREATE TABLE DATOSCLIENTES(
           Id INTEGER PRIMARY KEY AUTOINCREMENT,
           NOMBRE_USUARIO VARCHAR(50),
           PASSWORD VARCHAR(50),
           APELLIDO VARCHAR(10),
           DIRECCION VARCHAR(50),
           COMENTARIO VARCHAR(100))
           ''')
        messagebox.showinfo("BBDD","BBDD creada con éxito")
    except:
        messagebox.showwarning("!ATENCION!", "La BBDD ya existe")
        
def salirAplicacion():# para ejecutar el menú Salir
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    if valor=="yes":
        raiz.destroy()

def limpiarCampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0,END)# borra desde el primer al ultimo caracter

def crear():
    miConexion=sqlite3.connect("CLIENTES")
    miCursor=miConexion.cursor()   
    
    
    miCursor.execute("INSERT INTO DATOSCLIENTES VALUES (NULL,'" + miNombre.get() +
                     "','" + miPass.get()+
                     "','" + miApellido.get()+
                     "','" + miDireccion.get()+
                     "','" + textoComentario.get("1.0",END) + "')")
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con éxito")

def leer():
     miConexion=sqlite3.connect("CLIENTES")
     miCursor=miConexion.cursor()
     miCursor.execute("SELECT * FROM DATOSCLIENTES WHERE ID = "+ miId.get())
     elUsuario=miCursor.fetchall()

     for usuario in elUsuario:
         miId.set(usuario[0])
         miNombre.set(usuario[1])
         miPass.set(usuario[2])
         miApellido.set(usuario[3])
         miDireccion.set(usuario[4])
         textoComentario.insert(1.0,usuario[5])

     miConexion.commit()

def actualizar():
    miConexion=sqlite3.connect("CLIENTES")
    miCursor=miConexion.cursor()
    miCursor.execute("UPDATE  DATOSCLIENTES SET NOMBRE_USUARIO= ' "+ miNombre.get() +
                     "',PASSWORD='" + miPass.get()+
                     "',APELLIDO='" + miApellido.get()+
                     "',DIRECCION='" + miDireccion.get()+
                     "',COMENTARIO='" +textoComentario.get("1.0",END) + 
                     "' WHERE Id=" + miId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro actualizado con éxito")
    
    
def eliminar():
    miConexion=sqlite3.connect("CLIENTES")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSCLIENTES WHERE  ID=" + miId.get())
                     
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro borrado con éxito")

# --------------------------------------------------------------------------------------------

raiz=Tk() 

barraMenu=Menu(raiz)#menú  que cuelga de root.
raiz.config(menu=barraMenu,width=300,height=30)

bbddMenu=Menu(barraMenu,tearoff=0)#crea menú de base de datos.
bbddMenu.add_command(label="Conectar",command=conexionBBDD)#crear el texto del menu.
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)



crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)


#-------------COMIENZO DE CAMPOS--------------------------------------

miFrame=Frame(raiz)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()


cuadroID=Entry(miFrame,textvariable=miId)
cuadroID.grid(row=0,column=1,padx=10,pady=10)

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show ="?")

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)



#--------------------------------------------LABELS-----------------------

idLabel=Label(miFrame,text="ID :")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel=Label(miFrame,text="NOMBRE :")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passwordLabel=Label(miFrame,text="PASSWORD :")
passwordLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="APELLIDO :")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="DIRECCION:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)


comentariosLabel=Label(miFrame,text="COMENTARIOS :")
comentariosLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

# -------- AQUI VAN LOS BOTONES --------------------------------------

miFrame2=Frame(raiz)
miFrame2.pack()

botonCrear=Button(miFrame2,text="CREAR",command=crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="LEER",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Actualizar",command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Borrar" ,command=eliminar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)


raiz.mainloop()

