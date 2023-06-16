from afiliados import Afiliado
import csv

class ManejadorAfiliado:
    __afiliados: list[Afiliado]

    def __init__(self, path:str) -> None:
        self.__carga(path)

    def __carga(self, path:str):
        with open(path, "r") as file:
            lector=csv.reader(file, delimiter=";")
            next(lector,None)
            self.__afiliados=[Afiliado(fila) for fila in lector]

        for fila in self.__afiliados:
            print(f"{fila}")


    def obtenerNombre(self, dni:str) -> str:
        for afiliado in self.__afiliados:
            if afiliado.getDni() == dni:
                return afiliado.getNombre()
            
    def printOrdenado(self) -> None:
        self.__afiliados.sort()
        for afiliado in self.__afiliados:
            print(afiliado)

    def getDNIS(self) -> list:
        lista=[]
        for afiliado in self.__afiliados:
            lista.append(afiliado.getDni())
        return lista
    
