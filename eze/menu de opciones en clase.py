


opcion= -1

while opcion!=0:
    print("eliga alguna de las siguientes opciones:","\n","opcion1: superfiecie de un triangulo","\n","opcion2: cargar numero por serie","\n","opcion3: edad y nombre   ","\n","opcion4: pida una palabra","\n","opcion5:tuplas con meses y años" )
    opc=int(input("ingrese su opcion:"))

    if opc==1:
        base =float(input("ingrese la base :" ))
        alt=float(input("ingrese la altura:"))

        area= base*alt/2
    
        print ("la base y la altura de un triangulo es :",(area))

    

    elif opc==2:
        num =int(input("ingrese num"))
        contP=0
        may=0
    while (num<0):
        if (num %2==0):
            contP+=1
            may+=1
        elif num>may:
            may=num

        print("la cantidad de numero pares es:",(contP))
        print("el numero es mayor es ",(may))
    
        
    elif opc==3:

        nom=input("ingrese su nombre:")
        edad=(int(input("ingrese su edad:")

    while edad!=0:
        if edad>60:
            print("la persona es mayor de edad :"(edad))
        else:
            print("la edad es :"(edad,nom))
    

    elif opc==4:
        palabra=input("ingrese una palabra :")
    if palabra!=none:
        for i in range(10):
            print(palabra)
            palabra =  none

    elif opc==5:
        mes=("enero","febrero","marzo","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")





   

            

            
        
          


    
    
        
    
    
     



