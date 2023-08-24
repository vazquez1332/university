from __future__ import annotations
from typing import Any

class Celda: 
    __elemento: Any
    __siguiente: Celda | None

    def __init__(self, elemento) -> None:
        self.__elemento = elemento
        self.__siguiente = None

    def getElemento(self) -> Any:
        return self.__elemento
    
    def getSiguiente(self) -> Celda | None:
        return self.__siguiente
    
    def setSiguiente(self, sig) -> None:
        self.__siguiente = sig


class Pila:
    __size: int
    __tope: Celda | None

    def __init__(self) -> None:
        self.__size = 0
        self.__tope = None

    def __vacia(self) -> bool:
        return self.__size == 0
    
    def getSize(self) -> int:
        return self.__size
    
    def insertar(self, elemento: Any) -> None:
        c = Celda(elemento)
        c.setSiguiente(self.__tope)
        self.__tope = c
        self.__size += 1
        print("Elemento cargado.")

    def suprimir(self) -> Celda:
        if not self.__vacia():
            aux = self.__tope
            self.__tope = self.__tope.getSiguiente()
            self.__size -= 1

        return aux

    def recorrer(self) -> None:
        while not self.__vacia():
            print(self.suprimir().getElemento())

if __name__ == "__main__":
    p = Pila()

    p.insertar(1)
    p.insertar(2)
    p.insertar(3)
    p.insertar(4)
    p.insertar(5)

    p.recorrer()
     