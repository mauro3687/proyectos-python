from asyncore import loop


sexo =input("ingrese si sos m/f ")
edad=0
fem=0
mas=0
contM=0
contF=0
while (sexo=="M"or sexo =="F" ):
    edad=int(input("ingrese su edad:"))
#________parte1
    if sexo=="F":
       fem+=1
    elif sexo=="M":
      mas+=1
#_________parte2
    if sexo=="F" and edad>4 and edad<18:
        contF+=1
#_________parte3
    if sexo=="M"and edad<80:
        contM+=1
    sexo=input("ingrese si sos (M/F)")
if fem>mas:
    print("la mayor cantida de habitantes es femenina")
elif mas>fem:
    print("la mayor cantidad de habitantes es masculina")
else:
    print("los habitantes estan igual")
#FINAL TOTAL
print("la cantidad de femeninas en edad escolar es:",contF)
print("la cantidad de masculinos es :",contM)





  

    



    



    



    






