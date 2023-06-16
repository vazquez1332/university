from infractor import Infractor
from csv import reader

class GestorInfractores:
	__infractores: list

	def __init__(self, nombreArchivo):
		self.__infractores = []
		self.__leerArchivo(nombreArchivo)

	def encontrarInfractor(self, dni: str) -> None | Infractor:
		i = 0
		resultado = None

		while i < len(self.__infractores) and resultado is None:
			infractor = self.__infractores[i]

			if infractor.getDNI() == dni:
				resultado = infractor
			else:
				i += 1
		
		return resultado

	def obtenerListadoOrdenado(self) -> list:
		circulacionProhibida = []

		for infractor in self.__infractores:
			if infractor.getPuntaje() <= 0:
				circulacionProhibida.append(infractor)

		circulacionProhibida.sort()
		return circulacionProhibida

	def __leerArchivo(self, nombreArchivo):
		with open(nombreArchivo, 'r') as archivo:
			lector = reader(archivo, delimiter=';')
			next(lector, None)

			for fila in lector:
				self.__infractores.append(Infractor(fila))

