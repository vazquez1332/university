import numpy as np
from typing import Any

class Pila:
    __tope: int
    __size: int 
    __arreglo: np.ndarray

    def __init__(self, size: int = 999999) -> None:
        self.__tope = 0
        self.__size = size
        self.__arreglo = np.zeros(size)

    def vacia(self) -> bool:
        return self.__tope == 0
    
    def llena(self) -> bool:
        return self.__tope == self.__size
    
    def getTope(self) -> int:
        return self.__tope
    
    def apilar(self, elemento: Any) -> None:
        if not self.llena():
            self.__arreglo[self.__tope] = elemento
            self.__tope += 1
    
    def desapilar(self) -> int: 
        if not self.vacia():
            self.__tope -= 1
            elemento = self.__arreglo[self.__tope]
            self.__arreglo[self.__tope] = None

        return elemento
    
def factorial(num: int):
	pila = Pila()
	resultado: int = num
        
	while num != 2:
		num -= 1
		pila.apilar(num)

	while not pila.vacia():
		resultado *= pila.desapilar()

	return resultado

def factorialSinPila(num: int):
	resultado: int = num

	while num != 2:
		num -= 1
		resultado *= num

	return resultado

if __name__ == "__main__":
    print(factorial(123))
    