from ManejaHelados import ManejaHelados
from ManejaSabores import ManejaSabores
from os import system

class Menu:
    __maneja_sabores: ManejaSabores
    __maneja_helados: ManejaHelados
    __switch: dict

    def __init__(self) -> None:
        self.__maneja_sabores = ManejaSabores()
        self.__maneja_helados = ManejaHelados(self.__maneja_sabores)
        self.__switch = {
            1: self.opcion1,
            2: self.opcion2
           # 3: self.opcion3,
           # 4: self.opcion4,
           # 5: self.opcion5,
        }
        self.iniciar()

    def iniciar(self) -> None:
        self.menu()
        opcion = int(input("Ingrese la opcion: "))
        while opcion != 0:
            if opcion in self.__switch:
                self.__switch[opcion]()
            else: print("Opcion invalida, reingrese. ")

            system("pause")
            system("cls")

            self.menu()
            opcion = int(input("Ingrese la opcion: "))

    @staticmethod
    def menu() -> None:
        print("MENU DE OPCIONES")
        print("1- Registrar venta de helado. ")
        print("2- Mostrar el nombre de los cinco sabores mas pedidos. ")
        print("3- Gramos vendido por sabor. ")
        print("4- Informar sabores. ")
        print("5- Recaudo total. ")
        print("0- Para salir. ")

    def opcion1(self) -> None:
        pesos = [100, 150, 250, 500, 1000]
        print("\nLISTA DE PESOS")
        for peso in pesos:
            print(f"Peso en gr: {peso}")

        gr = float(input("Ingrese el peso del helado: "))
        if gr in pesos:
            precio = float(input("Ingrese el precio: "))
            if self.__maneja_helados.registrarHelado(gr, precio):
                print("Helado registrado. ")
        else: 
            print("Peso invalido. ")

    def opcion2(self) -> None:
        self.__maneja_sabores.masPedidos()