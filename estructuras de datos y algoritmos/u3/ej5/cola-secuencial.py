import numpy as np

class Cola:
    __items: np.ndarray
    __pr: int
    __ult: int
    __cant: int 
    __max: int 

    def __init__(self, max) -> None:
        self.__pr = 0
        self.__ult = 0
        self.__cant = 0
        self.__items = np.empty(max)
        self.__max = max 

    def vacia(self):
        return self.__cant == 0
    
    def llena(self): 
        return self.__cant == self.__max
    
    def insertar(self, item):
        if not self.llena():
            self.__items[self.__ult] = item
            self.__ult = (self.__ult + 1) % self.__max
            self.__cant += 1
    
    def suprimir(self):
        if not self.vacia():
            item = self.__items[self.__pr]
            del(self.__items[self.__pr]) 
            self.__pr = (self.__pr + 1) % self.__max
            self.__cant -= 1

        return item
    
    