import numpy as np

class Pila:
    __tope: int
    __tamaño: int
    __items: np.ndarray

    def __init__(self, tam):
        self.__tope = -1
        self.__tamaño = tam - 1
        self.__items = np.empty(tam)

    def vacia(self):
        return self.__tope == -1
    
    def llena(self):
        return self.__tope == self.__tamaño
    
    def insertar(self, item):
        if not self.llena():
            self.__tope += 1
            self.__items[self.__tope] = item
            print("Insertado.")

    def suprimir(self):
        if not self.vacia():
            item = self.__items[self.__tope]
            self.__items[self.__tope] = None
            self.__tope -= 1

        return item
    
    def recorrer(self):
        if not self.vacia():
            for item in self.__items[::-1]:
                print(item)

if __name__ == "__main__":
    p = Pila(5)
    
    p.insertar(1)
    p.insertar(2)
    p.insertar(3)
    p.insertar(4)
    p.insertar(5)

    p.recorrer()