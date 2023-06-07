from Empleado import Empleado
from Planta import Planta
from Contratado import Contratado
from Externo import Externo
from datetime import date
import numpy as np
import csv 


class ManejadorEmpleado:
    __arreglo: np.ndarray

    def __init__(self, len: int) -> None:
        self.__arreglo = np.empty(len, dtype = Empleado)
        self.__leer()
    
    def __leer(self) -> None:
        lista = []
        with open("contratados.csv", "r", encoding = "utf-8") as file:
            lector = csv.reader(file, delimiter = ";")
            next(lector)
            for fila in lector:
                lista.append(Contratado(fila))
        
        with open("externos.csv", "r", encoding = "utf-8") as file:
            lector = csv.reader(file, delimiter = ";")
            next(lector)
            for fila in lector:
                lista.append(Externo(fila))

        with open("planta.csv", "r", encoding = "utf-8") as file:
            lector = csv.reader(file, delimiter = ";")
            next(lector)
            for fila in lector:
                lista.append(Planta(fila))

        self.__arreglo = np.array(lista)

    def registrarHoras(self, dni: str, horas: int) -> None:
        i = 0 
        while i < len(self.__arreglo) and self.__arreglo[i].getDni() != dni:
            i += 1
        if i < len(self.__arreglo):
            self.__arreglo[i].addHoras(horas)
        else: 
            print("Empleados no encontrado")

    def buscarTarea(self, tarea: str) -> None:
        i = 0
        rango = len(self.__arreglo)
        while i < rango and not isinstance(self.__arreglo[i], Externo):
            i += 1
        if i < rango:
            while i < rango and self.__arreglo[i].getTarea() != tarea:
                i += 1
            if i < rango:
                hoy = str(date.today())
                if self.__arreglo[i].getFechaFin() > hoy:
                    print(f"El costo de la obra es: {self.__arreglo[i].getCosto()}")
        else:
            print("No se encontro la tarea")
