from typing import Any

class Nodo: 
    __dato: Any
    __izq: "Nodo" or None
    __der: "Nodo" or None

    def __init__(self, dato):
        self.__dato = dato
        self.__izq = None
        self.__der = None

    def getDato(self):
        return self.__dato
    
    def getIzq(self):
        return self.__izq
    
    def getDer(self):
        return self.__der
    
    def setIzq(self, izq):
        self.__izq = izq

    def setDer(self, der):
        self.__der = der           
