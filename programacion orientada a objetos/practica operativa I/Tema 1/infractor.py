"""
dni;nombre;apellido;direccion;numeroCarnet;puntaje
21111222;Andres;Ferreyra;Mitre 178;453311;10
"""

class Infractor:
	__dni: str
	__nombre: str
	__apellido: str
	__direccion: str
	__numeroCarnet: str
	__puntaje: int

	def __init__(self, linea):
		self.__dni = linea[0]
		self.__nombre = linea[1]
		self.__apellido = linea[2]
		self.__direccion = linea[3]
		self.__numeroCarnet = linea[4]
		self.__puntaje = int(linea[5])

	def getDNI(self):
		return self.__dni

	def descontarPuntaje(self, puntos: int):
		self.__puntaje -= puntos

	def getPuntaje(self):
		return self.__puntaje
	
	def getNombre(self):
		return self.__nombre

	def getApellido(self):
		return self.__apellido

	def getDireccion(self):
		return self.__direccion

	def getNumeroCarnet(self):
		return self.__numeroCarnet

	def __lt__(self, otro):
		if type(otro) != Infractor:
			raise TypeError("No se puede comparar un infractor con un objeto de otro tipo")
		
		resultado = None
		if self.__apellido == otro.getApellido():
			resultado = self.__nombre < otro.getNombre()
		else:
			resultado = self.__apellido < otro.getApellido()

		return resultado