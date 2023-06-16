from manejadorAtenciones import ManejadorAtenciones
from manejadorAfiliados import ManejadorAfiliado


class Menu:
    __manejador_atenciones: ManejadorAtenciones
    __manejador_afiliados: ManejadorAfiliado
    __switcher:dict

    def __init__(self, manejador1: ManejadorAtenciones , manejador2: ManejadorAfiliado) -> None:
        self.__manejador_atenciones=manejador1
        self.__manejador_afiliados=manejador2
        self.__switcher={
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4
        }
        self.procesar_opcion()

    def procesar_opcion(self) -> None:
        self.__mostrar_menu()
        opcion=int(input("\nIngrese la opcion: "))
        while opcion!=0:
            if opcion in self.__switcher:
                self.__switcher[opcion]()
            else: print("Opcion incorrecta. ")
            opcion=int(input("\nIngrese la opcion: "))

    def __mostrar_menu(self)->None:
        print("--------MENU--------")
        print("1: Buscar atencion ")
        print("2: Cantidad de atenciones por dni ")
        print("3: Lista de afilidos ordenada ")
        print("4: Afiliados que no tuvieron atencion ")
        print("0: Finalizar. ")

    def opcion1(self) -> None:
        fecha=input("Ingrese la fecha: ")
        entidad=input("Ingrese la entidad: ")
        self.__manejador_atenciones.buscarAtencion(fecha, entidad)

    def opcion2(self) -> None:
        dni=input("Ingrese el dni: ")
        self.__manejador_atenciones.buscarporDNI(dni)

    def opcion3(self) -> None:
        self.__manejador_afiliados.printOrdenado()

    def opcion4(self) -> None:
        self.__manejador_atenciones.sinAtenciones()
    