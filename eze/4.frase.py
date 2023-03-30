vocales='aeiou'
contV=0
contP=0
contPA=0
cantL=0
listaF=[]
frase=input("ingrese una frase:")
letra=input("ingrese una letra:")
for i in frase:
    if i in vocales:
        contV+=1
    if i.isalpha():
        cantL+=1
        if i ==" ":
            contP+=1
            
print("la cantidad de vocales son:",contV)
print("la cantidad de palabra es :",contP)
print("la cantidad de letras es:",cantL)
print("esta es la palabra en mayuscula",frase.upper())
print("esta es la palabra en minuscula",frase.lower())
