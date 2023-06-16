"""
dni;patente;tipoVehiculo;marca;fecha;descripcion;importeAPagar;Estado
31455111;AB011XZ;Auto;Fiat;06/05/2022;semaforo en rojo;45000;N
"""

class Infraccion:
	__dni: str
	__patente: str
	__tipoVehiculo: str
	__marca: str
	__fecha: str
	__descripcion: str
	__importe: float
	__estado: str

	def __init__(self, linea):
		self.__dni = linea[0]
		self.__patente = linea[1]
		self.__tipoVehiculo = linea[2]
		self.__marca = linea[3]
		self.__fecha = linea[4]
		self.__descripcion = linea[5]
		self.__importe = float(linea[6])
		self.__estado = linea[7]

	def getDNI(self):
		return self.__dni

	def getPatente(self):
		return self.__patente

	def getTipoVehiculo(self):
		return self.__tipoVehiculo

	def getMarca(self):
		return self.__marca

	def getDescripcion(self):
		return self.__descripcion

	def getImporte(self):
		return self.__importe

	def getEstado(self):
		return self.__estado

	def setEstado(self, estado: str):
		self.__estado = estado

	def __eq__(self, otro):
		if type(otro) != Infraccion:
			raise TypeError("No se puede comparar una infraccion con un objeto de otro tipo")

		return (
			self.__dni == otro.getDNI() and
			self.__patente == otro.getPatente() and
			self.__descripcion == otro.getDescripcion()
		)

		