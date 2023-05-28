import csv
from typing import List
from claseMateria import Materia

class Manejador_Materia:
    __lista: List["Materia"]

    def __init__(self,lista: List["Materia"])->None:
        self.__lista=lista
    
    @staticmethod
    def inicializar()->List[Materia]:
        lista=[]
        cabecera=True
        with open("materiasAprobadas.csv","r") as file:
            reader=csv.reader(file,delimiter=";")
            for fila in reader:
                if cabecera:
                    cabecera=not cabecera
                else:
                    lista.append(Materia(fila[0],fila[1],fila[2],fila[3],fila[4]))
       # for row in lista:
        #    print(f"{row} ")
        return lista
    
    def __str__(self)->str:
        return f"{[str(Materia) for Materia in self.__lista]}"

    def mostrar_promedio(self, dni:str)->None:
        prom_c_aplazos=[]
        prom_s_aplazos=[]
        self.__calcula_promedio(dni,prom_s_aplazos, prom_c_aplazos)
        print(f"DNI: {dni}")
        if prom_s_aplazos:
            print(f"Promedio sin aplazos: {sum(prom_s_aplazos)/len(prom_s_aplazos)}")
        else:
            print("No hay notas sin aplazos para calcular el promedio.")
        if prom_c_aplazos:
            print(f"Promedio con aplazos: {sum(prom_c_aplazos)/len(prom_c_aplazos)}")
        else:
            if prom_s_aplazos:
                print(f"Promedio con aplazos: {sum(prom_s_aplazos)/len(prom_s_aplazos)}")

    def __calcula_promedio(self, dni:str, lista1:list, lista2:list)->None:
        dni_encontrado=False
        for materia in self.__lista:
            if materia.getDni()==dni:
                dni_encontrado=True
                if materia.getNota() >= 4:
                    lista1.append(materia.getNota())
                else:
                    lista2.append(materia.getNota())
        if not dni_encontrado:
            print("DNI no encontrado.")

    def busca_promocional(self, materia:str)->List[Materia]:
        lista=[]
        for row in self.__lista:
            if row.getNombre()==materia and row.getNota()>=7 and row.getAprobacion()=="P":
               lista.append(row)
        return lista
            
    