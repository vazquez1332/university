from manejadorInscripcion import ManejadorInscripcion
from manejadorPersona import ManejadorPersona
from manejadorTaller import ManejadorTaller

class Menu:
    __manejador_inscripcion: ManejadorInscripcion
    __manejador_persona: ManejadorPersona
    __manejador_taller: ManejadorTaller
    __options: dict

    def __init__(self, manejador1: ManejadorInscripcion, manejador2: ManejadorPersona, manejador3: ManejadorTaller) -> None:
        self.__manejador_inscripcion = manejador1
        self.__manejador_persona = manejador2
        self.__manejador_taller = manejador3
        self.__options = {
            1: self.opcion1,
            2: self.opcion2,
        #    3: self.opcion3,
        #    4: self.opcion4,
            5: self.opcion5
        }
        self.__procesar()

    def __procesar(self) -> None:
        self.__menu()
        opcion = int(input("\nIngrese la opcion: "))
        while opcion != 0:
            if opcion in self.__options:
                self.__options[opcion]()
            else:
                print("Opcion incorrecta")
            self.__menu()
            opcion = int(input("\nIngrese la opcion: "))

    def __menu(self) -> None:
        print("\n----MENU DE OPCIONES----")
        print("1- Inscribir una persona en un taller")
        print("2- Consultar inscripcion")
        print("3- Consultar inscriptos")
        print("4- Registrar pagos")
        print("5- Guardar inscripciones")
        print("0- Para salir")

    def opcion1(self) -> None:
        self.__manejador_taller.mostrar()
        self.__manejador_inscripcion.registrarInscripcion(self.__manejador_taller.obtenerTaller(input("\nIngrese el nombre del taller: ")), self.__manejador_persona.registarPersona())
    
    def opcion2(self) -> None:
        self.__manejador_inscripcion.buscarInscripto(input("Ingrese el dni: "))

    def opcion5(self) -> None:
        self.__manejador_inscripcion.generarArchivo()
        