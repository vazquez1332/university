import numpy as np

class Pila:
    __tope: int
    __tamaño: int
    __items: np.ndarray

    def __init__(self, tam = 999999):
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

    def suprimir(self):
        if not self.vacia():
            item = self.__items[self.__tope]
            self.__items[self.__tope] = None
            self.__tope -= 1

        return item
    
def factorial(num):
	pila = Pila()
	resultado = num
        
	while num != 2:
		num -= 1
		pila.insertar(num)

	while not pila.vacia():
		resultado *= pila.suprimir()

	return resultado

if __name__ == "__main__":
    print(factorial(123))