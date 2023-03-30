import FALSE, TRUE

class Cabañitas:
    def __init__(self,Nom,dni,canTU,monT,Cod):
        self.Nombre=Nom
        self.DNI=dni
        self.cantidad_Ucupante=canTU
        self.monto=monT
        self.codigo=Cod

def CA_alquile(alquiler):
    n=len (alquiler)

    for i in range (n):
        Nom=input("ingrese su NOMBRE:"
        )
        dni=int(input("ingrese su ducumento el reservante:"))
        canTU=int(input("ingrese la cantidad de ocupantes:"))
        monT=int(input("ingrese el monto del alquiler que adquirio")
        )
        Cod=validar()
        alquiler[i]=cabaña(Nom,dni,canTU,monT,Cod)

def validar ():
    n=int(input("ingrese el codigo de alquiler del (1-5):"))
    return n

def inprimir_alquileres(alquiler):
    n=len(alquiler)
    for i in range(n):
        print("el nombre que reservo la cabaña es :",alquiler[i].Nombre)
        print("el dni de que reservo es :",alquiler[i].DNI)
        print("la cantidad que ocupa la cabaña es :",alquiler[i].cantidad_Ucupante)
        print("el monto para alquilar es :",alquiler[i].monto)
        print("el codigo del alquiler es:",alquiler[i].codigo)

def cant_monto(alquiler):
    n=len(alquiler)
    acum=0
    x=int(input("ingrese el monto:")
    )
    for i in range(n):
        if alquiler[i].m_A < x:
            acum+=1
            print("LOS ALQUILERES CON UN  MONTO  MAYOR A ",x,"SON",acum)



def MC(alquiler):
    n=len(alquiler)
    C1=0
    C2=0
    C3=0
    C4=0
    C5=0
    for i in range (n):
        if alquiler [i].monto==1:
            C1+=alquiler[i].monto
        elif alquiler[i].monto==2:
            C2+=alquiler[i].monto
        elif alquiler [i].monto==3:
            C3+=alquiler[i].monto
        elif alquiler [i].monto==4:
            C4+=alquiler[i].monto
        elif alquiler [i].monto==5:
            C5+=alquiler[i].monto
    print("el  monto la cabaña tipo 1 es:",C1)
    print("el  monto la cabaña tipo 2 es:",C2)
    print("el  monto la cabaña tipo 3 es:",C3)
    print("el  monto la cabaña tipo 4 es:",C4)
    print("el  monto la cabaña tipo 5 es:",C5)


def MM(alquier):
    n=len(alquiler)
    x=9999999999999999
    NOMBRE=0
    DNII=0
    for i in range (n):
        if alquiler[i].monto > x:
            x==alquiler[i].monto
            NOMBRE=alquiler[i].nombre
            DNII=alquiler[i].dni
    print("la cantidad  de ocupantes en todas las cabañas es:",acum)
    print("la cantidad de cabañas ocupadas son :",acum1)

def salir ():
    print("CERRADO SECION")












def MENU(alquiler):
    n=len(alquiler)
    GS=FALSE
    if n>=2:
        GS=TRUE
    else:
        GS=FALSE
    op=int(input("opcion(1):cargar alquileres","\n","opcion(2):mostrar los alquileres,","\n","opcion(3):cantidad  de alquileres con un monto mayor :","\n","opcion(4):monto total  de tipo de cabañs:","\n","opcion(5):alquiler  con menor monto:","\n","opcion(6):alquiler con mayor de monto del alquiler:","\n","opcion(7):total de ocupantes en todas las cabañas y sus cantidad reservada","\n","opcion(8):salir:","\n",))
        if op==1:
            CA_alquile(alquiler)
            MENU(alquiler)
        elif  GS== TRUE and op==2:
            inprimir_alquileres(alquiler)
            MENU(alquiler)
        elif  GS==TRUE and op==3:
            cant_monto(alquiler)
            MENU(alquiler)
        elif  GS==TRUE and op==4:
            MC(alquiler)
            MENU(alquiler)
        elif  GS==TRUE and op==5:
            MM(alquiler)
            MENU(alquiler)
        elif  GS==TRUE and op==6:
            MY(alquiler)
            MENU(alquiler)
        elif  GS==TRUE and op==7:
            MY(alquiler)
            MENU(alquiler)
        elif op==8:
            salir ()
            

def Principal():
    R=int(input("ingrese la cantidad de alquiles:" ))
    alquires=R*[None]
    MENU(alquiler)

        
        




    
        


