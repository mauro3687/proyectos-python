import random
numero="123456789"
letras='abcdefghijklmop'
total_licencia=1
nom=input("ingrese su nombre ")
ape=input("ingrese su apellido")
mar=input("ingrese marca de su vehiculo")
modelo=input("ingrese el modelo del vehiculo")
col=input("ingrese el color de su vehiculo")

for i in range(total_licencia):
    nro1 = random.choice(numero)
    nro2 =random.choice(numero)
    nro3 =random.choice(numero)
    

    l1=random.choice(letras)
    l2=random.choice(letras)
    l3=random.choice(letras)
    l4=random.choice(letras)

print("apellido del titular: ",(ape)"\n","nombre del titular ",(nom)"\n","marca del vehiculo",(mar)"\n","color del vehiculo",(col)"\n"
      "la patente generada es:",l1,l2,nro1,nro2,nro3,l3,l4)



    
    
    
    

    
