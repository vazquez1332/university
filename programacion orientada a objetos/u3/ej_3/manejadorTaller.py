from Taller import TallerCapacitacion
import numpy as np
import csv

class ManejadorTaller:
    __arreglo: np.ndarray

    def __init__(self) -> None:
        cant = True
        i = 0
        with open("Talleres.csv", "r", encoding = "utf-8") as file:
            lector = csv.reader(file, delimiter=";")
            for fila in lector:
                if cant:
                    self.__arreglo = np.empty(shape = int(fila[0]), dtype = TallerCapacitacion)
                    cant = not cant
                else:
                    self.__arreglo[i] = (TallerCapacitacion(fila))
                    i += 1

    def mostrar(self) -> None:
        for i in range(len(self.__arreglo)):
            print("\n----Taller----")
            print(f"id: {self.__arreglo[i].getId()}")
            print(f"nombre: {self.__arreglo[i].getNombre()}")
            print(f"vacantes: {self.__arreglo[i].getVacantes()}")
            print(f"monto: {self.__arreglo[i].getMonto()}")

    def obtenerTaller(self, nomb: str) -> TallerCapacitacion:
        i = 0
        while i != len(self.__arreglo) and self.__arreglo[i].getNombre() != nomb:
            i += 1
        if i < len(self.__arreglo):
            if self.vacantes(self.__arreglo[i]):
                return self.__arreglo[i]
        else:
            print("Taller no encontrado")

    def vacantes(self, taller: TallerCapacitacion) -> bool:
        if taller.getVacantes() > 0:
            taller.setVacantes()
            return True
        else:
            print("Taller sin vacantes")