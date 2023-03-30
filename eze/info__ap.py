
lista=[]
lista2=[]
n = int(input("Ingrese la cantidad de modelos a ingresar"))

for x in range(n):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)
    valor2= input("Ingrese el modelo:")
    lista2.append(valor2)

#print(lista)

posicion=0
while posicion<len(lista):
    if lista[posicion]> 20000:
        lista.pop(posicion)
        lista2.pop(posicion)

    else:
        posicion=+1
    
print(lista)
print(lista2)
