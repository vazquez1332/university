# Tabla Hash
# Manejo de Colisiones: Buckets

import numpy as np

class TablaHash:
    __dimension : int
    __tabla : np.ndarray
    __dimensionBucket: int
    __comienzoOverflow: int

    def __init__(self, numeros, dimensionBucket):
        self.__dimension = (numeros/dimensionBucket) 
        self.__dimension += self.__dimension*0.2
        self.__dimensionBucket = dimensionBucket
        self.__comienzoOverflow = self.__dimension - (self.__dimension*0.2)

        self.__tabla = np.empty((self.__dimension, self.__dimensionBucket), dtype=int)
        for i in range(0, self.__dimension):
            for j in range(0, self.__dimensionBucket):
                self.__tabla[i][j] = 0
    

    def metodoExtraccionClaves(self, valor, dimension): #Explicacion: extrae el ultimo digito de cada numero como clave para la tabla hash
        valor = valor % 10 #Ejemplo: 123 -> 123 % 100 = 23
        return valor % dimension

    def insertar(self, valor):
        direccion = self.metodoExtraccionClaves(valor, self.__dimension)
        j = 0
        while j < self.__dimensionBucket and self.__tabla[direccion][j] != 0:
            j += 1
        if j < self.__dimensionBucket:
            self.__tabla[direccion][j] = valor

        else:
            print("No se pudo insertar")
    
    def buscar(self, valor):
        direccion = self.metodoExtraccionClaves(valor, self.__dimension)
        j = 0
        while j < self.__dimensionBucket and self.__tabla[direccion][j] != valor:
            j += 1
        if j < self.__dimensionBucket:
            return True
        else:
            return False

    def mostrar(self):
        print("#Tabla Hash")
        for i in range(0,self.__dimension):
            print("\nDireccion: ", i)
            for j in range(0,self.__dimensionBucket):
                print("{}:{}".format(j,self.__tabla[i][j]), end="    ")
            print("")
        print("\n\n")
        print("#Tabla Overflow")
        for i in range(0, self.__dimensionOverflow):
            print("\nDireccion: ", i)
            for j in range(0, self.__dimensionBucket):
                print("{}:{}".format(j,self.__tablaOverflow[i][j]), end="   ")
            print("")
    
if __name__ == "__main__":
    th = TablaHash(10, 3)
    th.insertar(123)
    th.insertar(323)
    th.insertar(453)
    th.insertar(553)
    th.insertar(456)
    th.insertar(789)

    th.mostrar()