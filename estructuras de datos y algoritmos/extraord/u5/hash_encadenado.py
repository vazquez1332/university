import numpy as np
from lista import lista

class EncadenamientoHash:
    __dimension: int # Dimensión de la tabla hash
    __tabla = None # Tabla hash

    def __init__(self, dimension):
        self.__dimension = self.getPrimo(int(dimension//0.7)) # Calcula el número primo más cercano a dimension//0.7
        self.__tabla = np.empty(self.__dimension, dtype=lista) # Inicializa la tabla hash con el número primo calculado

        for i in range(0,self.__dimension): # Inicializa cada posición de la tabla hash con None
            self.__tabla[i] = None

    def getPrimo(self, numero): # Función para encontrar el número primo más cercano a un número dado
        for i in range(2, numero): # Comprueba si el número es divisible por cualquier número hasta él mismo
            if numero % i == 0: # Si es divisible, llama a la función de nuevo con el número incrementado en 1
                return self.getPrimo(numero+1)
        return numero # Si no es divisible por ningún número, devuelve el número

    def metodoPlegado(self, valor): # Método para calcular la dirección de un valor en la tabla hash
        acumulador = 0 # Inicializa un acumulador con 0

        while valor != 0: # Mientras el valor no sea 0
            acumulador += valor % 10 # Suma la última cifra de valor al acumulador
            valor //= 10 # Elimina la última cifra de valor

        return acumulador % self.__dimension # Devuelve el módulo de acumulador y la dimensión de la tabla hash

    def insertarHash(self, valor): # Método para insertar un valor en la tabla hash
        direccion = self.metodoPlegado(valor) # Calcula la dirección de valor en la tabla hash
        if self.__tabla[direccion] == None: # Si la posición en la tabla hash en la dirección calculada está vacía
            self.__tabla[direccion] = lista() # Crea una nueva lista lista en esa posición
        self.__tabla[direccion].insertarLista(valor) # Inserta valor en la lista encadenada en esa posición


    def buscar(self, valor):
        direccion = self.metodoPlegado(valor)
        if self.__tabla[direccion] == None: #type: ignore
            return "No se encontro el valor"
        else:
            return direccion

