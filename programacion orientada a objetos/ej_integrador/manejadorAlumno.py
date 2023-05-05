import csv
import numpy as np
from numpy import ndarray
from claseAlumno import Alumno

class Manejador_Alumno:
    __arreglo: ndarray

    def __init__(self, array:ndarray)->None:
        self.__arreglo=array

    @staticmethod
    def inicializar()->ndarray:
        array=np.empty((8), dtype=Alumno)
        cabecera=True
        i=0
        with open("alumnos.csv","r") as file:
            reader=csv.reader(file,delimiter=";")
            for fila in reader:
                if cabecera:
                    cabecera=not cabecera
                else: 
                    array[i]=Alumno(fila[0], fila[1], fila[2], fila[3], fila[4])
                    i+=1
       # for i in range(len(array)):
        #    print(f"{array[i]} ")
        return array
    
    def __str__(self)->str:
        return f"{[str(Alumno) for Alumno in self.__arreglo]}"
     
    def busca_alumno(self,dni:str)->"Alumno":
        i=0
        while i<len(self.__arreglo) and self.__arreglo[i].getDni()!=dni:
            i+=1
        if i<len(self.__arreglo):
            return self.__arreglo[i]
        else: print("No se encuentra el dni. ")
        
    def ordenar(self)->list[Alumno]:
        return sorted(self.__arreglo)