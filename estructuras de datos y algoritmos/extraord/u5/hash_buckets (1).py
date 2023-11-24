import numpy as np

class TablaHash:
    __dimension : int
    __tabla : np.ndarray
    __dimensionOverflow: int
    __dimensionBucket: int
    __dimensionTotal: int

    def __init__(self, dimension, dimensionBucket):
        # Se calcula la dimensión de la tabla principal como el número primo más cercano a la dimensión dada dividida por 0.7.
        # Esto se hace para mantener un factor de carga de 0.7.
        self.__dimension = self.getPrimo(int(dimension//0.7)) 
        # La dimensión de la tabla de desbordamiento es el 20% de la dimensión de la tabla principal.
        self.__dimensionOverflow = int(self.__dimension *0.2)
        self.__dimensionTotal = self.__dimension + self.__dimensionOverflow
        self.__dimensionBucket = dimensionBucket

        # Se inicializan la tabla principal.
        self.__tabla = np.empty((self.__dimensionTotal, self.__dimensionBucket), dtype=int)
        # Se inicializan las tablas con ceros.

        for i in range(0, self.__dimension):
            for j in range(0, self.__dimensionBucket):
                self.__tabla[i][j] = 0
    
    
    def getPrimo(self, numero):
        # Este método devuelve el número primo más cercano a un número dado.
        for i in range(2, numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        return numero

    def metodoExtraccionClaves(self, valor, dimension): 
        # Este método extrae el último dígito de un número como clave para la tabla hash.
        valor = valor % 10 
        return valor % dimension

    def insertar(self, valor):
        # Se calcula la dirección en la tabla hash para el valor dado.
        direccion = self.metodoExtraccionClaves(valor, self.__dimension)
        j = 0
        # Se busca un bucket vacío en la dirección calculada en la tabla principal.
        while self.__tabla[direccion][j] != 0 and j < self.__dimensionBucket:
            j += 1
        if j < self.__dimensionBucket:
            # Si hay un bucket vacío, se inserta el valor allí.
            self.__tabla[direccion][j] = valor
        else:
            print("Zonda de desbordamiento")
            # Si no hay buckets vacíos en la tabla principal, se calcula una nueva dirección para la tabla de desbordamiento.
            direccion = self.metodoExtraccionClaves(valor, (self.__dimensionTotal - self.__dimensionBucket))
            j = 0
            # Se busca un bucket vacío en la dirección calculada en la tabla de desbordamiento.
            while self.__tabla[direccion][j] != 0 and j < self.__dimensionBucket:
                j += 1
            if j < self.__dimensionBucket:
                # Si hay un bucket vacío, se inserta el valor allí.
                self.__tabla[direccion][j] = valor
            else:
                # Si no hay buckets vacíos en la tabla de desbordamiento, se imprime un mensaje de error.
                print("No se pudo insertar")
    
    def buscar(self, valor):
        # Se calcula la dirección en la tabla hash para el valor dado.
        direccion = self.metodoExtraccionClaves(valor, self.__dimension)
        j = 0
        # Se busca el valor en los buckets de la dirección calculada en la tabla principal.
        while j < self.__dimensionBucket and self.__tabla[direccion][j] != valor:
            j += 1
        if j < self.__dimensionBucket:
            # Si se encuentra el valor, se devuelve True.
            return True
        else:
            # Si no se encuentra el valor en la tabla principal, se busca en la tabla de desbordamiento.
            direccion = self.metodoExtraccionClaves(valor, (self.__dimensionTotal - self.__dimensionBucket))
            j = 0
            while j < self.__dimensionBucket and self.__tabla[direccion][j] != valor:
                j += 1
            if j < self.__dimensionBucket:
                # Si se encuentra el valor en la tabla de desbordamiento, se devuelve True.
                return True
            else:
                # Si no se encuentra el valor en ninguna de las tablas, se devuelve False.
                return False
