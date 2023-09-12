import numpy as np

class Disco:
	__tamaño: int

	def __init__(self, tamaño: int):
		self.__tamaño = tamaño

	def getTamaño(self):
		return self.__tamaño

class Torre: 
	__arreglo: np.ndarray
	__tope: int
	__size: int

	def __init__(self, size: int = 100):
		self.__arreglo = np.full(size, None)
		self.__tope = 0
		self.__size = size
	
	def cantidadDiscos(self):
		return self.__tope

	def vacia(self):
		return self.__tope == 0

	def añadirDisco(self, elem):
		if self.__tope == self.__size:
			raise Exception('La pila esta llena')

		self.__arreglo[self.__tope] = elem
		self.__tope += 1

	def quitarDisco(self):
		if self.__tope == 0:
			raise Exception('No quedan elementos en la pila')
		
		self.__tope -= 1
		valor = self.__arreglo[self.__tope]
		self.__arreglo[self.__tope] = None
		return valor

	def tamañoUltimoDisco(self):
		if(self.vacia()):
			return "La pila esta vacia"

		return self.__arreglo[self.__tope - 1].getTamaño()

	def getTamañoDisco(self, i: int):
		value = self.__arreglo[i - 1]
		if value is None:
			return ' '

		return str(value.getTamaño())