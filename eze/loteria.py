import random
numero=[]
for i in range(15):
   n=random.randint(1,100)
   numero.append(n)
print(n)



print(" Tiene 3 Oportunidades Para Acertarle A los Numeros Ganadores")
z=int(input("Ingrese un Numero"))
x=int(input("Ingrese un Numero"))
y=int(input("Ingrese un Numero"))

if z in numero or x in numero or y in numero:
   print("A Acertado A Alguno De Los Numeros")
else:
   ("No A Acertado Ninguno")
        
