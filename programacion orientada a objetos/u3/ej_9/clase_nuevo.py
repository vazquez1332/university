from clase_vehiculo import Vehiculo

class Vehiculonuevo(Vehiculo):
    def __init__(self, modelo, cantPuertas, color, precioVenta, marca, version):
        super().__init__(modelo, cantPuertas, color, precioVenta, marca)
        self.__version = version

    def importe(self):
        importe = self.getPrecioVenta() + (0.1*self.getPrecioVenta())
        if self.__version == "full":
            importe += self.getPrecioVenta() * 0.02
        return importe 
    
    def getPrecioVenta(self):
        return super().getPrecio()
    
    def getClass(self):
        return str(self.__class__.__name__)
    
    def getPatente(self):
        return None
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                modelo = super().getModelo(),
                cantPuertas = super().getPuertas(),
                color = super().getColor(),
                precioVenta = super().getPrecio(),
                marca = super().getMarca(),
                version = self.__version
                )
            )
        return d

    
