v=0
contP=1
contV=0
cantL=0
Vocles=["a","e","i","o","u"]
frase=input("ingrese una frase ")
for i in frase:
    if i in Vocles:
       contV+=1
    if i.isalpha():
        i.isalpha()
        cantL+=1
        if i ==" " :
            contP+=1
porle=(contV*100)/cantL
print("la cantidad de vocales:",contV)
print("la cantidad de letras es: ",cantL)
print("la cantida de palabra es :",contP)
print("el porsentaje es ",porle,"%")

    

    


    
        

