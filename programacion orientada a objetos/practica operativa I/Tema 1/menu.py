from gestorInfracciones import GestorInfracciones
from gestorInfractores import GestorInfractores

class Menu:
	__infracciones: GestorInfracciones
	__infractores: GestorInfractores

	def __init__(self, infracciones: GestorInfracciones, infractores: GestorInfractores):
		self.__infracciones = infracciones
		self.__infractores = infractores

	def mostrarMenu(self):
		print("0. Salir")
		print("1. Mostrar infracciones")
		print("2. Pagar infracciones")
		print("3. Mostrar si es reincidente reincidentes")
		print("4. Mostrar infractores con circulacion prohibida")

	def opcion1(self):
		dni = input("Ingrese el dni del infractor: ")
		infractor = self.__infractores.encontrarInfractor(dni)
		if infractor is None:
			print("El infractor no existe")
		else:
			print('Datos del infractor')
			print('Apellido: %10s    Nombre: %10s    DNI: %10s' % (infractor.getApellido(), infractor.getNombre(), infractor.getDNI()))
			print('Carnet: %10s    Dirección: %20s' % (infractor.getNumeroCarnet(), infractor.getDireccion()))

			print('infracciones')
			print ('pantente    tipo del vehiculo    marca          descripcion       importe')

			infracciones = self.__infracciones.obtenerInfracciones(dni)
			total = 0

			for infrac in infracciones:
				if infrac.getEstado() == 'N':
					print('%s %15s %15s %25s %10s' % (infrac.getPatente(), infrac.getTipoVehiculo(), infrac.getMarca(), infrac.getDescripcion(), infrac.getImporte()))
					total += infrac.getImporte()

			descuento = 0
			if len(infracciones) == 0 and self.__infracciones.obtenerNumeroInfraccionesIguales(dni) == 1:
				descuento = total * 0.5

			print('SUBTOTAL: %10s' % total)
			print('DESCUENTO: %10s' % descuento)
			print('TOTAL: %10s' % (total - descuento))
			
	def opcion2(self):
		dni = input("Ingrese el dni del infractor: ")
		patente = input("Ingrese la patente del vehiculo: ")

		self.__infracciones.marcarInfraccionesPagadas(dni, patente)

	def opcion3(self):
		dni = input("Ingrese el dni del infractor: ")
		conteo = self.__infracciones.obtenerNumeroInfraccionesIguales(dni)

		if conteo >= 3:
			print("El infractor es reincidente")
		else:
			print("El infractor no es reincidente")

	def opcion4(self):
		listado = self.__infractores.obtenerListadoOrdenado()

		print('Listado de infractores con circulacion prohibida')
		for infractor in listado:
			print('Apellido: %10s    Nombre: %10s    DNI: %10s    Puntaje: %10s' % (infractor.getApellido(), infractor.getNombre(), infractor.getDNI(), infractor.getPuntaje()))

	def iniciar(self):
		self.mostrarMenu()
		print('\n')
		opcion = input("Ingrese una opcion: ")
		print('\n')

		if opcion == "1":
			self.opcion1()
		elif opcion == "2":
			self.opcion2()
		elif opcion == "3":
			self.opcion3()
		elif opcion == "4":
			self.opcion4()
		
		print('\n')
		if opcion != '0':
			self.iniciar()