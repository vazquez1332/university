import numpy as np
from typing import Any

class Pila:
    __tope: int
    __size: int 
    __arreglo = None

    def __init__(self, size: int) -> None:
        self.__tope = 0
        self.__size = size
        self.__arreglo = np.empty(size)

    def __vacia(self) -> bool:
        return self.__tope == 0
    
    def __llena(self) -> bool:
        return self.__tope == self.__size
    
    def getTope(self) -> int:
        return self.__tope
    
    def apilar(self, elemento: Any) -> None:
        if not self.__llena():
            self.__arreglo[self.__tope] = elemento
            self.__tope += 1
            print("Carga exitosa.")
    
    def desapilar(self) -> int: 
        if not self.__vacia():
            self.__tope -= 1
            elemento = self.__arreglo[self.__tope]
            self.__arreglo[self.__tope] = None

        return elemento
    
    def print(self):
        while not self.__vacia():
            print(self.desapilar())
    

if __name__ == "__main__":
    p = Pila(5)

    p.apilar(1)
    p.apilar(2)
    p.apilar(3)
    p.apilar(4)
    p.apilar(5)

    p.print()
