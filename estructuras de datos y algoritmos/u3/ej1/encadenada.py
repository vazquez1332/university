from typing import Any

class Celda:
    __item: Any
    __siguiente: "Celda"

    def __init__(self, item):
        self.__item = item
        self.__siguiente = None

    def getItem(self):
        return self.__item
    
    def setSig(self, sig):
        self.__siguiente = sig
    
    def getSig(self):
        return self.__siguiente
    
class Pila:
    __cant: int
    __tope: "Celda"

    def __init__(self):
        self.__cant = 0
        self.__tope = None

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, item):
        c = Celda(item)
        c.setSig(self.__tope)
        self.__tope = c
        self.__cant += 1

    def suprimir(self):
        if not self.vacia():
            aux = self.__tope
            self.__tope = aux.getSig()
            self.__cant -= 1

        return aux
    

        