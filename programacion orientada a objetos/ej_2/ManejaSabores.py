from Sabor import Sabor
import csv 
import numpy as np

class ManejaSabores:
    __lista: list[Sabor]
    __cont: np.ndarray

    def __init__(self) -> None:
        self.__carga()

    def __carga(self) -> None:
        with open("sabores.csv", "r") as file:
            lector = csv.reader(file, delimiter=";")
            self.__lista = [Sabor(fila) for fila in lector]
            self.__cont = np.zeros(len(self.__lista))

    def obtenerSabor(self, id: int) -> Sabor:
        if id in range(len(self.__lista)):
            return self.__lista[id]
        else:
            print("Sabor no encontrado.")

    def listaSabores(self) -> None:
        print("\nLISTA DE SABORES")
        for sabor in self.__lista:
            print(sabor)

    def contarSabores(self, id: int) -> None:
        if id in range(len(self.__cont)):
            self.__cont[id] += 1

    def masPedidos(self) -> None:
        maspedidos = np.argsort(self.__cont)[::-1]
        print("Sabores mas pedidos: ")
        for i in range(4):
            print(self.obtenerSabor(maspedidos[i]).getNombre())
    

        
        