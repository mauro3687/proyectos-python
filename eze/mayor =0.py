

num=0
mayor=0
menor=15
acum=0
mayprom=0
lista=[]
for i in range (10):
    num=int(input("ingresar num:"))
    lista.append(num)
    acum+=num
    if num>mayor:
        mayor=num
    if num<menor:
         menor=num
promedio=acum//10
for i in lista:
    if i> promedio:
        mayprom+=1
print("El numero mayor es:",+ (mayor))
print("El num

     


