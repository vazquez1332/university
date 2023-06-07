from ManejaFacultades import ManejadorFacultad
from os import system

class Menu:
    __maneja_facultades: ManejadorFacultad
    __switch: dict

    def __init__(self, manejador: ManejadorFacultad) -> None:
        self.__maneja_facultades = manejador
        self.__switch = {
            1: self.opcion1,
            2: self.opcion2
        }
        self.__iniciar()


    def __iniciar(self) -> None:
        self.__mostrarMenu()
        opcion = int(input("Ingrese la opcion: "))
        while opcion != 0:
            if opcion in self.__switch:
                self.__switch[opcion]()

            else: print("Opcion invalida, reingrese. ")

            system("pause")
            system("cls")
            self.__mostrarMenu()
            opcion = int(input("Ingrese la opcion: "))

    def __mostrarMenu(self) -> None:
        print("         ----MENU----        ")
        print("""1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre 
        y duración de cada una de las carreras que se dictan en esa facultad.""")
        print("""2. Dado el nombre de una carrera, mostrar código,
        nombre y localidad de la facultad donde esta se dicta.""")
        print("0. Finalizar. ")
        
    def opcion1(self) -> None:
        self.__maneja_facultades.codigo_obtener(int(input("Ingrese el codigo de la facultad: ")))
    
    def opcion2(self) -> None:
        self.__maneja_facultades.nombre_obtener(input("Ingrese el nombre de la carrera: "))

        