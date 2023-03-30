n=int(input("ingrese la cantidad de numero que sea ingresar"))
nro=0 
for i in range (n):
    num=int(input("ingrese un numero:"))
    if i==0:
        var=num
    if num<nro:
        print("los numero son ignorados" )
print("los numero son mayores",nro)


