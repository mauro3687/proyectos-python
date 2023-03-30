class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar (self):
        self.enmarcha=True
    def estado (self):
        if (self.enmarcha):
            return"el coche esta en marcha"
        else:
            return"el coche esta detenido"

miCoche=Coche()
print ("el largo de coche es :",miCoche.largoChasis)
print("el coche tiene ",miCoche.ruedas,"ruedas")
miCoche.arrancar()
print(miCoche.estado())
   
