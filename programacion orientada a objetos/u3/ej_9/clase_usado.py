from clase_vehiculo import Vehiculo

class VehiculoUsado(Vehiculo):
    def __init__(self, modelo, cantPuertas, color, precioVenta, marca, patente, anio, kilometraje):
        super().__init__(modelo, cantPuertas, color, precioVenta, marca)
        self.__patente = patente
        self.__anio = int(anio)
        self.__kilometraje = int(kilometraje)
        
    def importe(self, anioActual = 2023):
        importe = self.getPrecioVenta() - ((self.getPrecioVenta()*0.01) * (anioActual - self.__anio))
        if self.__kilometraje > 100000:
            importe -= (self.getPrecioVenta()*0.02)
        return importe
    
    def getPrecioVenta(self):
        return super().getPrecio()

    def getClass(self):
        return str(self.__class__.__name__)
    
    def getPatente(self):
        return self.__patente
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                modelo = super().getModelo(),
                cantPuertas = super().getPuertas(),
                color = super().getColor(),
                precioVenta = super().getPrecio(),
                marca = super().getMarca(),
                patente = self.__patente,
                anio = self.__anio,
                kilometraje = self.__kilometraje,
                )
            )
        return d
    
