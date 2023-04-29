import csv
from typing import List

class Viajero:
    __num_viajero: int
    __dni:str
    __nombre: str
    __apellido: str
    __millas_acum: int

    def __init__(self, v1:str, v2:str, v3:str, v4:str, v5: str):
        self.__num_viajero=int(v1)
        self.__dni=v2
        self.__nombre=v3
        self.__apellido=v4
        self.__millas_acum=int(v5)

    def cantidadTotaldeMillas(self)->int:
        return self.__millas_acum
    
    def acumularMillas(self, cant)->int:
        self.__millas_acum+=cant
        return self.__millas_acum
    
    def canjearMillas(self, c:int)->bool:
        if self.__millas_acum>=c:
            self.__millas_acum-=c
            print("Canje exitoso.\n")
        else:
            print("Error, millas insuficientes.\n")
            return False
    
    def getMillasAcum(self):
        return self.__millas_acum
    
    def __repr__(self)->str:
        return f"{self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum}"
    
    @staticmethod
    def opening()->List["Viajero"]:
        viajeros=[]
        with open("viajeros.csv","r") as file:
            reader=csv.reader(file, delimiter=",")
            for fila in reader:
                viajeros.append(Viajero(
                    fila[0], fila[1], fila[2], 
                    fila[3], fila[4]))
        return viajeros
    
    @staticmethod
    def obtenerViajero(num:int, lista:List["Viajero"])->"Viajero":
        i=0
        while i<len(lista) and lista[i].__num_viajero != num:
            i+=1
        if(i == len(lista)):
            raise ValueError("Viajero inexistente.\n")
        return lista[i]
    
    @staticmethod
    def Menu():
        print("\nMENU\n")
        print("1- Consultar Cantidad de Millas\n2- Acumular Millas\n3- Canjear Millas\n0- Salir\n")
    

    
    


            