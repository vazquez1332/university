from Inscripcion import Inscripcion
from Persona import Persona
from Taller import TallerCapacitacion
import numpy as np
import datetime
import csv

class ManejadorInscripcion:
    __arreglo: np.ndarray 

    def __init__(self) -> None:
        self.__arreglo = np.array([])
    
    def registrarInscripcion(self, taller: TallerCapacitacion, persona: Persona,) -> None:
        lista = []
        fecha = str(datetime.date.today())
        lista.append(Inscripcion(fecha, persona, taller))
        self.__arreglo = np.append(self.__arreglo, lista)
    
    def buscarInscripto (self, dni:str)-> None:
        i = 0

        while i < len(self.__arreglo) and self.__arreglo[i].getPersona().getDni() != dni:
             i+=1 

        if i < len(self.__arreglo):
            taller = self.__arreglo[i].getTaller()
            print(f"Taller: {taller.getNombre()}")
            print(f"Monto que adeuda: {taller.getMonto()}")

        else: print("Persona no encontrada")


    def generarArchivo(self) -> None:
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])

        with open("Inscripciones.csv", "w", newline = "") as file:
            escritor = csv.writer(file, delimiter=";")
            for i in range(len(self.__arreglo)):
                lista = []
                lista.append(self.__arreglo[i].getPersona().getDni())
                lista.append(self.__arreglo[i].getTaller().getId())
                lista.append(self.__arreglo[i].getFecha())
                lista.append(self.__arreglo[i].getPago())
                escritor.writerow(lista)

