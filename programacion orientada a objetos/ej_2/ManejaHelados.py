from Helado import Helado
from ManejaSabores import ManejaSabores

class ManejaHelados:
    __lista: list[Helado]
    __maneja_sabores: ManejaSabores

    def __init__(self, manejador: ManejaSabores) -> None:
        self.__lista = []
        self.__maneja_sabores = manejador

    def registrarHelado(self, peso: float, precio: float) -> bool:
        helado = Helado(peso, precio)
        rango = int(input("\nCuantos sabores va a llevar? (MAXIMO 4): "))
        self.__maneja_sabores.listaSabores()

        i = 0
        print("\nElija los sabores")
        while i < rango:
            id = int(input("Ingrese el id del sabor: ")) - 1
            helado.setSabor(self.__maneja_sabores.obtenerSabor(id))
            self.__maneja_sabores.contarSabores(id)
            i += 1
        return True