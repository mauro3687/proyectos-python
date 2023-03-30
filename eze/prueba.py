class VEnta:
    
    def __init__(self,CVent,Cvend,Ctv,mont):
        self.codigoVenta=CVent
        self.codigoVendedor=Cvend
        self.tipoVenta=Ctv
        self.monto=mont

def MVenta(venta):
    n=len(venta)
    CaV_mayor=0
    CaV=0
    for i in range(n):
        if Venta[i].monto>CaV_mayor:
            CaV_mayor=venta[i].monto
            CaV=Venta.codigoVenta


def mostrarVentas(Venta):
    n=len(Venta)
    acum=0
    for i in range (n):
        print("La venta ingresada",Venta,"es:")
        print("el codigo de la venta es:",Venta[i].codigoVenta)
        print("el codigo del vendedor es:",codigoVendedor)
        print("el tipo de la venta es:",Venta[i].tipoVenta)
        print("el monto de la venta es:",Venta[i].monto)
        acum=+1




def VENTA(Venta):
    n=len(Venta)
    for i in range(n):
        CVent=int(input("ingrese el codigo de ventas: "))
        Cvend= Vendedor()
        Ctv= TipoVenta()
        mont=int(input("ingrese el monto de la venta: "))
        Venta[i]=VEnta(CVent,Cvend,Ctv,mont)
    print("CARGA finalizada")







def Vendedor():
    n=int(input("ingrese el codigo del vendedor (1-4): "))
    while n < 1 or n > 4:
        print("Error!! deve ingresar nuevamente el codigo del vendedor(1-4)")
        n=int(input("ingrese el codigo del vendedor (1-4): "))
        return n    



def TipoVenta():
    x=int(input("ingrese el tipo de venta (1-2): "))
    while x <1 or x>2:
        print("Error!! deve ingresar nuevamente el codigo de tipo de venta(1-2)")
        x=int(input("ingrese el tipo de venta (1-2): "))
        return x  





def Principal ():
    
    cantV=int(input("ingrese la cantidad de ventas a ingresar"))
    Venta=cantV*[None]
    VENTA(Venta)


Principal()
