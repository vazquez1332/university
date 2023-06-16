import numpy as np
from csv import reader
from infraccion import Infraccion
from gestorInfractores import GestorInfractores

class GestorInfracciones:
	__infracciones: np.ndarray
	__infractores: GestorInfractores

	def __leerArchivo(self, archivo):
		with open(archivo, 'r') as archivo:
			lector = reader(archivo, delimiter=';')
			next(lector, None)

			for fila in lector:
				infraccion = Infraccion(fila)
				infractor = self.__infractores.encontrarInfractor(infraccion.getDNI())

				if infractor is not None:
					self.__infracciones = np.append(self.__infracciones, infraccion) # type: ignore
					infractor.descontarPuntaje(10)

	def __init__(self, archivo: str, infractores: GestorInfractores):
		self.__infracciones = np.empty(0, dtype=Infraccion)
		self.__infractores = infractores
		self.__leerArchivo(archivo)

	def obtenerInfracciones(self, dni: str) -> list:
		resultado = []

		for infraccion in self.__infracciones:
			if infraccion.getDNI() == dni:
				resultado.append(infraccion)

		return resultado

	def obtenerNumeroInfraccionesIguales(self, dni: str) -> int:
		resultado = 0

		for infraccion in self.__infracciones:
			if infraccion.getDNI() == dni:
				cont = 0
			
				for infraccion2 in self.__infracciones:
					if infraccion == infraccion2:
						cont += 1

				if cont > resultado:
					resultado = cont

		return resultado

	def marcarInfraccionesPagadas(self, dni: str, patente: str):
		for infraccion in self.__infracciones:
			if infraccion.getDNI() == dni and infraccion.getPatente() == patente and infraccion.getEstado() == 'N':
				infraccion.setEstado('P')
