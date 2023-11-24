import os
import numpy as np
from lista import lista

class DigrafoEncadenado:
    __arreglo: np.ndarray
    __cantidadV: int

    def __init__(self, cantidadV):
        self.__cantidadV = cantidadV
        self.__arreglo = np.empty(cantidadV, dtype=lista)

        # Inicializar cada lista
        for i in range(cantidadV):
            self.__arreglo[i] = lista()
    
    def crearArista(self, i, j):
        if (i <= self.__cantidadV and j <= self.__cantidadV) and (i >= 0 and j >= 0):
            self.__arreglo[i].insertar(j)
        else:
            print("Error: vertices no validos")

    def getAdyacentes(self, vertice):
        lista = []
        aux = self.__arreglo[vertice].getCabeza()
        
        while aux is not None: 
            lista.append(aux.getDato())  # Obtiene la lista de vértices adyacentes
            aux = aux.getSig()
        else:
            print("Error: vertice no valido")
        
        return lista
    
    def esConexo(self):
        visitados = self.rep(self.NodoFuente())
        if len(visitados) == self.__cantidadV:
            return True 
        else:
            return False
        
    def esAciclico(self):
        for i in range(self.__cantidadV):
            if self.esAciclicoRec(i, visitados=[False] * self.__cantidadV, padre=-1):
                return False
        return True
    
    def esAciclicoRec(self, vertice, visitados, padre):
        visitados[vertice] = True
        
        v = self.__arreglo[vertice].getCabeza()
        while v is not None:
            if not visitados[v.getDato()]:
                if self.esAciclicoRec(v.getDato(), visitados, vertice):
                    return True
            elif padre != v.getDato():
                return True
        return False
    
    def rea(self, verticeInicial): #Recorrido en anchura
        lista = []
        visitados = [False] * self.__cantidadV
        cola = [verticeInicial]

        while cola:
            vertice = cola.pop(0)
            lista.append(vertice)
            visitados[vertice] = True
            
            v = self.__arreglo[vertice].getCabeza()
            while v is not None:
                if not visitados[v.getDato()]:
                    cola.append(v.getDato())
                    visitados[v.getDato()] = True
                v = v.getSiguiente()
        
        return lista
    
    def rep(self, verticeInicial): #Recorrido en profundidad
        lista = []
        self.repRec(verticeInicial, [False] * self.__cantidadV, lista)
        return lista
        
    def repRec(self, vertice, visitados, lista):
        visitados[vertice] = True
        lista.append(vertice)
        
        cabeza = self.__arreglo[vertice].getCabeza()
        while cabeza is not None:
            if not visitados[cabeza.getDato()]:
                self.repRec(cabeza.getDato(), visitados, lista)
            cabeza = cabeza.getSiguiente()
 
    def camino(self, verticeInicial, verticeFinal):
        return verticeFinal in self.rep(verticeInicial)
           
    #Adicionales Digrafo
    def gradoDeEntrada(self, vertice):
        grado = 0
        for i in range(self.__CantidadV):
            if self.__matriz[i][vertice] == 1: #type: ignore
                grado += 1
        return grado

    def gradoDeSalida(self, vertice):
        return len(self.obtenerAdyacentes(vertice))
    
    #Nodo fuente: evalua si vertice es nodo funete
    def nodoFuente(self, vertice):
        if self.gradoEntrada(vertice) == 0 and self.gradoSalida(vertice) > 0:
            return True
        return False
    
    #Nodo sumidero: evalua si vertice es nodo sumidero
    def nodoSumidero(self, vertice):
        if self.gradoSalida(vertice) == 0 and self.gradoEntrada(vertice) > 0:
            return True
        return False
    
    #Otros metodos
    def mostrarDigrafo(self):
        for i in range(self.__cantidadV):
            print(f'{i} --> ', end='')

            lista_vecinos = self.__arreglo[i].getCabeza()  # Obtener la cabeza de la lista
            while lista_vecinos is not None:
                print(f'{lista_vecinos.getDato()} --> ', end='')
                lista_vecinos = lista_vecinos.getSiguiente()
            
            print("None")  # Marcar el final de los vecinos
    
