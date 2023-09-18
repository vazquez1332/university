from typing import Any

class Celda:
    __item: Any 
    __sig: "Celda"
    
    def __init__(self, item):
        self.__item = item

    def getItem(self):
        return self.__item
    
    def setSig(self, sig):
        self.__sig = sig

    def getSig(self):
        return self.__sig
    
class Cola:
    __cant: int
    __pr: "Celda"
    __ult: "Celda"

    def __init__(self):
        self.__cant = 0
        self.__pr = None
        self.__ult = None

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, item):
        c = Celda(item)
        c.setSig(None)

        if self.__ult == None:
            self.__pr = c
        
        else:
            self.__ult.setSig(c)

        self.__ult = c 
        self.__cant += 1

    def suprimir(self):
        if not self.vacia():
            aux = self.__pr
            self.__pr = aux.getSig()
            self.__cant -= 1

        return aux.getItem()
    
    