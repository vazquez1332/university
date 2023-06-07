class Vehiculo():
    def __init__(self, modelo, cantPuertas, color, precioVenta, marca):
        self.__modelo = modelo 
        self.__cantPuertas = cantPuertas
        self.__color = color 
        self.__precioVenta = precioVenta
        self.__marca = marca

    def importe(self):
        return float(self.__precioVenta)
    
    def getModelo(self):
        return self.__modelo
    
    def getPuertas(self):
        return self.__cantPuertas
    
    def getColor(self):
        return self.__color
    
    def getPrecio(self):
        return float(self.__precioVenta)
    
    def getMarca(self):
        return self.__marca

    def setPrecio(self, precio):
        self.__precioVenta = precio
        
    def __str__(self):
        cadena = self.__modelo + " "
        cadena += self.__cantPuertas + " "
        cadena += str(self.importe())
        return cadena 