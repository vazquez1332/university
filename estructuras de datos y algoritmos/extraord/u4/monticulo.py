import numpy as np

class Monticulo:
    # Estos son los atributos de la clase Monticulo. 
    # __arreglo es el arreglo que representa el montículo, __cantidad es el número de elementos en el montículo y __dimension es el tamaño máximo del montículo.
    __arreglo : np.ndarray
    __cantidad : int
    __dimension : int

    # Este es el constructor de la clase. Se inicializa el arreglo con un tamaño especificado y se establece la cantidad de elementos a 0.
    def __init__(self, dimension):
        self.__arreglo = np.empty(dimension, dtype = int)
        self.__cantidad = 0
        self.__arreglo[0] = 0
        self.__dimension = dimension
    
    # Este método verifica si el montículo está vacío. Devuelve True si la cantidad de elementos es 0, es decir, si el montículo está vacío.
    def vacio(self):
        return self.__cantidad == 0

    # Este método verifica si el montículo está lleno. Devuelve True si la cantidad de elementos es igual a la dimensión del montículo, es decir, si el montículo está lleno.
    def lleno(self):
        return self.__cantidad == self.__dimension
    
    # Estos métodos devuelven la posición del padre, del hijo izquierdo y del hijo derecho de un nodo en el montículo, respectivamente.
    def Padre(self, posicion):
        return posicion // 2
    
    def hijoIzquierdo(self, posicion):
        return posicion * 2

    def hijoDerecho(self, posicion):
        return (posicion * 2) + 1

    # Este método intercambia los elementos en las posiciones pos1 y pos2 en el arreglo.
    def intercambiar(self, pos1, pos2):
        aux = self.__arreglo[pos1]
        self.__arreglo[pos1] = self.__arreglo[pos2]
        self.__arreglo[pos2] = aux
    
    # Este método verifica si un nodo es una hoja. Devuelve True si la posición del nodo es mayor que la cantidad de elementos en el montículo, es decir, si el nodo es una hoja.
    def esHoja(self, posicion):
        return posicion > self.__cantidad 

    # Este método inserta un nuevo elemento en el montículo. Si el montículo está lleno, imprime un mensaje de error. De lo contrario, inserta el elemento y luego reordena el montículo para mantener la propiedad de montículo mínimo.
    def insertar(self, dato):  
        if self.lleno(): # Verifica si el montículo está lleno.
            print("Montículo lleno") # Si está lleno, imprime un mensaje y termina el método.
        else:
            self.__cantidad += 1 # Si no está lleno, incrementa la cantidad de elementos en el montículo.
            self.__arreglo[self.__cantidad] = dato # Inserta el nuevo dato en la última posición del montículo.
            pos = self.__cantidad # Guarda la posición del nuevo dato.

            padre = self.Padre(pos) # Obtiene la posición del padre del nuevo dato.

            # Mientras el nuevo dato sea menor que su padre, intercambia las posiciones del dato y su padre.
            while self.__arreglo[pos] < self.__arreglo[padre]: 
                self.intercambiar(pos, padre) 
                pos = padre # Actualiza la posición del dato.
                padre = self.Padre(pos) # Actualiza la posición del padre.


    # Este método elimina el elemento mínimo del montículo. Si el montículo está vacío, imprime un mensaje de error. De lo contrario, elimina el elemento mínimo, reordena el montículo y devuelve el elemento eliminado.
    def eliminar(self): 
        if self.vacio(): # Verifica si el montículo está vacío.
            print("Montículo vacío") # Si está vacío, imprime un mensaje y termina el método.
        else:
            eliminado = self.__arreglo[1] # Guarda el elemento mínimo del montículo (la raíz).
            self.__arreglo[1] = self.__arreglo[self.__cantidad] # Reemplaza la raíz con el último elemento del montículo.
            self.__arreglo[self.__cantidad] = 0 # Elimina el último elemento del montículo.
            self.__cantidad -= 1 # Decrementa la cantidad de elementos en el montículo.
            self.eliminar_minimo(1) # Reordena el montículo para mantener la propiedad de montículo mínimo.
            return eliminado # Devuelve el elemento eliminado.
        
        
    # Este método reordena el montículo después de eliminar el elemento mínimo. Se intercambian los nodos padre e hijo hasta que el nodo padre es menor que sus hijos.
    def eliminar_minimo(self, padre):
        hijoIzq = self.hijoIzquierdo(padre) # Obtiene la posición del hijo izquierdo del nodo padre.
        hijoDer = self.hijoDerecho(padre) # Obtiene la posición del hijo derecho del nodo padre.

        # Mientras el nodo padre no sea una hoja y sea mayor que alguno de sus hijos, intercambia las posiciones del nodo padre y su hijo menor.
        while not self.esHoja(hijoDer) and (self.__arreglo[padre] > self.__arreglo[hijoIzq] or self.__arreglo[padre] > self.__arreglo[hijoDer]):
            if self.__arreglo[hijoIzq] < self.__arreglo[hijoDer]: # Si el hijo izquierdo es menor que el hijo derecho, intercambia las posiciones del nodo padre y su hijo izquierdo.
                self.intercambiar(padre, hijoIzq)
                padre = hijoIzq # Actualiza la posición del nodo padre.
            else: # Si el hijo derecho es menor que el hijo izquierdo, intercambia las posiciones del nodo padre y su hijo derecho.
                self.intercambiar(padre, hijoDer)
                padre = hijoDer # Actualiza la posición del nodo padre.
            hijoIzq = self.hijoIzquierdo(padre) # Actualiza la posición del hijo izquierdo.
            hijoDer = self.hijoDerecho(padre) # Actualiza la posición del hijo derecho.

