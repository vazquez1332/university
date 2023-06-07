from clase_personal import Personal

class Nodo:
    __personal: Personal
    __siguiente: object

    def __init__(self,personal):
        self.__personal = personal
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__personal
    
    def setDato(self, dato):
        self.__personal = dato