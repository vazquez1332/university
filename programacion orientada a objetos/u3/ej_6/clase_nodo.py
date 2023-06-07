from clase_vehiculo import Vehiculo

class Nodo:
    __vehiculo: Vehiculo
    __siguiente: object

    def __init__(self,vehiculo):
        self.__vehiculo = vehiculo
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__vehiculo