import random
nro=int(input("ingrease un numero" ))
listI=[]
listP=[]
listT=[]
acum=0

for i in range (nro):
   n= random.randing(1,200)
   listT.append(n)
   acum=0
   if n %2==0:
    listP.append(n);
else:
    listI.append(n)

print("la cantidad de numero totales es:",listT)
print("la cantidad de numero pares es :",listP)
print("la cantidad de numero impares es :",listI)




   




    

  
