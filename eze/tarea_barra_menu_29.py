from tkinter import*

from tkinter import messagebox
import sqlite3

#________funciones_____
def conexionBbdd():#crean conexion entre base datos y menu
    miConexion=sqlite3.connect("CLIENTES")
    miCursor=miConexion.cursor()


#_________funcines______
def salirAplicacion():
    valor=messagebox.askquestion("salir","¿desea salir de la aplicaion?")
    if valor == "yes":
      raiz.destroy()

      
      
      
      
raiz =Tk()
miFrame =Frame(raiz,width=1200,height=600)
miFrame.pack()
    


barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)
archivoBbdd=Menu(barraMenu,tearoff=0)

archivoBbdd.add_command(label="Conectar")
archivoBbdd.add_command(label="Salir",command=salirAplicacion)

archivoBorrar=Menu(barraMenu,tearoff=0)
archivoBorrar.add_command(label="Borrar campo")

archivoCrud=Menu(barraMenu,tearoff=0)

archivoCrud.add_command(label="Crear")
archivoCrud.add_command(label="Leer")
archivoCrud.add_command(label="actualizar")
archivoCrud.add_command(label="Borrar")


archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de....")

barraMenu.add_cascade(label="Bbdd",menu=archivoBbdd)
barraMenu.add_cascade(label="Borrar",menu=archivoBorrar)
barraMenu.add_cascade(label="Crud",menu=archivoCrud)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

#________ cuadros de texto____

cuadroID=Entry(miFrame)
cuadroID.grid(row=0,column=1)
cuadroID.config(fg="red",justify="center")

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1,column=1)
cuadroNombre.config(fg="blue" ,justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1)
cuadroApellido.config(fg="orange" ,justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1)
cuadroPass.config(fg="pink" ,justify="center")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4,column=1)
cuadroDireccion.config(fg="orange" ,justify="center")

textoComentario=Text(miFrame,width=15,height=15)
textoComentario.grid(row=5,column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")

#____ETIQUETA___
IDLabel=Label(miFrame,text="ID")
IDLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

NombreLabel=Label(miFrame,text="NOMBRE")
NombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

ApellidoLabel=Label(miFrame,text="APELLIDO")
ApellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

PassLabel=Label(miFrame,text="PASS")
PassLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

DireccionLabel=Label(miFrame,text="DIRECCION")
DireccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)


ComentarioLabel=Label(miFrame,text="COMENTARIO")
ComentarioLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#___BOTON_____
miFrame2=Frame(raiz)
miFrame2.pack()

botonCrear=Button(miFrame2,text="CREATE")
botonCrear.grid(row=1,column=0,sticky="e",pady=10,padx=10)


botonRead=Button(miFrame2,text="READ")
botonRead.grid(row=1,column=1,sticky="e",pady=10,padx=10)
    

botonUpdate=Button(miFrame2,text="UPDATE")
botonUpdate.grid(row=1,column=2,sticky="e",pady=10,padx=10)

botonDelete=Button(miFrame2,text="DELETE")
botonDelete.grid(row=1,column=3,sticky="e",pady=10,padx=10)






















