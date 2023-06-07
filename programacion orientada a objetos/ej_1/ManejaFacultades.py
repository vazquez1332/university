from Facultad import Facultad
import csv

class ManejadorFacultad:
    __lista: list[Facultad]

    def __init__(self) -> None:
        self.__lista = []
        self.__carga("Facultades.csv")

    def __carga(self, path: str) -> None:
        with open(path,"r", encoding="utf-8") as file:
            lector = csv.reader(file, delimiter=",")
            for fila in lector:
                if "Facultad" in fila[1]:
                    facultad = Facultad(fila)
                    self.__lista.append(facultad)
                else: 
                    facultad.setCarrera(fila)

    def codigo_obtener(self, codigo: int) -> None:
        i = 0
        while i < len(self.__lista) and codigo != self.__lista[i].getCodigo():
            i += 1
        if i < len(self.__lista):
            print(f"Facultad: {self.__lista[i].getNombre()}")
            for carrera in self.__lista[i].getCarreras():
                print(carrera)
        else:
            print("No se encontró la facultad. ")

    def nombre_obtener(self, nombre: str) -> None:
        i = 0
        j = 0
        found = True
        while i < len(self.__lista) and found:
            facultad = self.__lista[i]
            while j < len(facultad.getCarreras()) and facultad.getCarreras()[j].getNombre() != nombre: 
                j += 1
            if j < len(facultad.getCarreras()):
                print(f"Codigo: {facultad.getCodigo()},{facultad.getCarreras()[j].getCodigo()}")
                print(f"Nombre de facultad: {facultad.getNombre()}")
                print(f"Localidad: {facultad.getLocalidad()}")
                found = not found
            else:
                print("No se encontro la carrera. ")
                i += 1
        
