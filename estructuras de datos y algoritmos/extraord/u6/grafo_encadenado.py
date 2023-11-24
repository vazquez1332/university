import os
import numpy as np
from lista import lista

class GrafoEncadenado:
    __arreglo: np.ndarray
    __cantidadV: int

    # Constructor de la clase
    def __init__(self, cantidadV: int):
        self.__cantidadV = cantidadV  # Número de vértices
        self.__arreglo = np.empty(cantidadV, dtype=lista)  # Inicializa el arreglo con listas encadenadas

        # Inicializar cada lista
        for i in range(cantidadV):
            self.__arreglo[i] = lista()  # Cada vértice tiene su propia lista encadenada para almacenar sus vértices adyacentes
    
    # Método para agregar una arista al grafo
    def insertarArista(self, origen, destino):
        self.__arreglo[origen].insertar(destino)  # Inserta el destino en la lista del vértice origen
        self.__arreglo[destino].insertar(origen)  # Como es un grafo no dirigido, también inserta el origen en la lista del vértice destino
            
    # Método para obtener los vértices adyacentes a un vértice dado
    def getAdyacentes(self, vertice):
        lista = []
        aux = self.__arreglo[vertice].getCabeza()
        
        while aux is not None: 
            lista.append(aux.getDato())  # Obtiene la lista de vértices adyacentes
            aux = aux.getSig()
        else:
            print("Error: vertice no valido")
        
        return lista

    # Método para verificar si el grafo es conexo
    def esConexo(self):
        return len(self.rea(0)) == self.__cantidadV  # Si el número de vértices visitados es igual al número total de vértices, el grafo es conexo

    # Método para verificar si el grafo es acíclico
    def esAciclico(self):
        for i in range(self.__cantidadV):
            if self.esAciclicoRecursivo(i, [False] * self.__cantidadV, -1):  # Si se encuentra un ciclo, el grafo no es acíclico
                return False
        return True

    # Método auxiliar para verificar si el grafo es acíclico
    def esAciclicoRecursivo(self, vertice, visitados, padre):
        visitados[vertice] = True  # Marca el vértice como visitado

        # Iterar a través de la lista encadenada del vértice
        nodo = self.__arreglo[vertice].getCabeza()
        while nodo is not None:
            vecino = nodo.getDato()

            # Si el vecino no ha sido visitado, intentar encontrar un ciclo desde él
            if not visitados[vecino]:
                if self.esAciclicoRecursivo(vecino, visitados, vertice):
                    return True

            # Si el vecino ya ha sido visitado y no es el padre del vértice actual, se encontró un ciclo
            elif vecino != padre:
                return True

            nodo = nodo.getSiguiente()

        return False
    
    # Método para realizar un recorrido en anchura del grafo
    def rea (self, verticeInicial): 
        lista = []
        visitados = [False] * self.__cantidadV
        cola = [verticeInicial]

        while cola:
            vertice = cola.pop(0)
            lista.append(vertice)
            visitados[vertice] = True
            
            # Iterar a través de la lista encadenada del vértice
            nodo = self.__arreglo[vertice].getCabeza()
            while nodo is not None:
                vecino = nodo.getDato()
                if not visitados[vecino]:
                    cola.append(vecino)
                    visitados[vecino] = True
                nodo = nodo.getSiguiente()
        
        return lista

    # Método auxiliar para realizar un recorrido en profundidad del grafo
    def rep (self, verticeInicial): 
        lista = []
        self.repRec(verticeInicial, [False] * self.__cantidadV, lista)
        return lista

    def repRec(self, verticeInicial, visitados, lista):
        visitados[verticeInicial] = True
        lista.append(verticeInicial)
        
        nodo = self.__arreglo[verticeInicial].getCabeza()
        while nodo is not None:
            vecino = nodo.getDato()
            if not visitados[vecino]:
                self.repRec(vecino, visitados, lista)
            nodo = nodo.getSiguiente()
    
    def camino(self, origen, destino):
        return destino in self.rep(origen)
