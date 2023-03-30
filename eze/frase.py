import random
cant=0
v=0
palabra=1
l=0
vocal=("a","e","i","o","u")
frase=input("ingrese una frase: ")
letra=input("ingrese una letra: ")

for i in frase:
   if frase.isalpha():
      cant+=1
   if i in vocal:
      v+=1
   if i== " ":
      palabra+=1
   if letra==vocal:
      l+=1
   if i in letra:
      l+=1
                      
print("la cantidad de veces que aparece la letra seleccionada es: ",l)
print("la cantidad de vocales en la frase es: ",v)
print("la cantidad de palabras en la frase es: ",palabra) 
print(frase.upper())
print(frase.lower())       
