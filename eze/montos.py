com=float(input("ingrese la compra"))
while (com!=-1):
    com=float(input("ingrese otra vez que no sea negativa"))
    if (com<1000):
        descuento=(com%10)/100
    
     print("el total a pagar es:",(descuento))
else:
     print("el total a pagar es:",(com))


              
  
