from tkinter import*
raiz =Tk()
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)
archivoBbdd=Menu(barraMenu,tearoff=0)
archivoBbdd.add_command(label="Conectar")
archivoBbdd.add_command(label="Salir")

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



