print("MI COCHE 2")
class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=2
    enmarcha=False

   
    def estado (self):
        if (self.enmarcha):
            return"el coche esta en marcha"
        else:
            return"el coche esta detenido"

miCoche=Coche()
print ("el largo de coche es :",miCoche.largoChasis)
print("el coche tiene ",miCoche.ruedas,"ruedas")

print(miCoche.estado())

#mi coche 2_________________
print("*********************")
print("mi coche 1")

   
class Coche2():
    largoChasis=300
    anchoChasis=200
    ruedas=4
    enmarcha=False

    def arrancar (self):
        self.enmarcha=True
    def estado (self):
        if (self.enmarcha):
            return"el coche esta en marcha"
        else:
            return"el coche esta detenido"

miCoche2=Coche2()
print ("el largo de coche es :",miCoche2.largoChasis)
print("el coche tiene ",miCoche2.ruedas,"ruedas")
miCoche2.arrancar()
print(miCoche2.estado())
