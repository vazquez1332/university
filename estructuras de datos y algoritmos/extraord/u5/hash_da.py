import numpy as np  # Importa el módulo numpy para operaciones de matriz

class tablaHash_DA:  # Define la clase tablaHash_DA
    __dimension : int  # Declara una variable privada para almacenar la dimensión de la tabla hash
    __tabla : np.ndarray  # Declara una variable privada para almacenar la tabla hash
    __contador : int  # Declara una variable privada para contar el número de colisiones

    def __init__(self, dimension):  # Método de inicialización para la clase
        self.__dimension = int(dimension//0.7)  # Establece la dimensión de la tabla hash
        self.__tabla = np.empty(self.__dimension, dtype= int)  # Crea una matriz numpy vacía de la dimensión especificada
        self.__contador = 0  # Inicializa el contador a 0

        for i in range(0,self.__dimension):  # Llena la tabla hash con ceros
            self.__tabla[i] = 0

    def metodoDivision(self, valor):  # Define el método de transformación de claves
        return valor % self.__dimension  # Devuelve el módulo del valor proporcionado y la dimensión de la tabla

    def insertar(self, valor):  # Define el método para insertar un valor en la tabla hash
        direccion = self.metodoDivision(valor)  # Calcula la dirección en la tabla hash
        j = 0  # Inicializa el contador de iteraciones
        if self.__tabla[direccion] == 0:  # Si la posición calculada está vacía
            self.__tabla[direccion] = valor  # Inserta el valor
        else:  # Si la posición calculada no está vacía
            while self.__tabla[direccion] != valor and self.__tabla[direccion] != 0 and j<self.__dimension:  # Mientras la posición no esté vacía y no se haya encontrado el valor
                self.__contador += 1  # Incrementa el contador de colisiones
                direccion = (direccion + 1) % self.__dimension  # Calcula la siguiente dirección
                j += 1  # Incrementa el contador de iteraciones

            if j<self.__dimension and self.__tabla[direccion] == 0:  # Si se encontró una posición vacía
                self.__tabla[direccion] = valor  # Inserta el valor

    def buscar(self, valor):  # Define el método para buscar un valor en la tabla hash
        direccion = self.metodoDivision(valor)  # Calcula la dirección en la tabla hash
        j = 0  # Inicializa el contador de iteraciones

        while self.__tabla[direccion] != valor and self.__tabla[direccion] != 0 and j<self.__dimension:  # Mientras la posición no esté vacía y no se haya encontrado el valor
            direccion = (direccion + 1) % self.__dimension  # Calcula la siguiente dirección
            j += 1  # Incrementa el contador de iteraciones

        if self.__tabla[direccion] == valor:  # Si se encontró el valor
            return direccion  # Devuelve la dirección del valor
        else:  # Si no se encontró el valor
            return -1  # Devuelve -1

    def mostrar(self):  # Define el método para imprimir la tabla hash
        for i in range(0, self.__dimension):  # Para cada posición en la tabla hash
            print("Posicion: ", i, " Valor: ", self.__tabla[i])  # Imprime la posición y el valor

    def promedioColisiones(self):  # Define el método para calcular el promedio de colisiones
        return self.__contador/self.__dimension  # Devuelve el promedio de colisiones

"""La clase tablaHash_DA_primo es similar a tablaHash_DA, pero utiliza un número primo para la dimensión de la tabla hash. 
Esto puede ayudar a reducir las colisiones en la tabla hash."""

class tablaHash_DA_primo: #Direccionamiento Abierto (DA) con num primo para la dimension
    __dimension : int
    __tabla : np.ndarray
    __contador : int

    def __init__(self, dimension):
        self.__dimension = self.getPrimo(int(dimension//0.7)) #Factor de carga = 0.7
        self.__tabla = np.empty(self.__dimension, dtype= int)
        self.__contador = 0

        for i in range(0,self.__dimension):
            self.__tabla[i] = 0
    
    def getPrimo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        return numero
    
"""¿Cuál de los dos métodos es más eficiente? ¿Por qué?
   El metodo de direccionamiento abierto con numero primo es mas eficiente, ya que 
   el factor de carga es menor, por lo que la probabilidad de colisiones es menor.
   ademas, el metodo de direccionamiento abierto con numero primo tiene una menor
   cantidad de colisiones que el metodo de direccionamiento abierto normal.  
    
Sin embargo, hay que tener en cuenta que el método de división puede no funcionar bien
si el tamaño de la tabla hash es un número que tiene factores comunes con las claves. 
Por ejemplo, si el tamaño de la tabla hash es un número par y las claves son todas números pares,
todas las claves se mapearán a posiciones pares en la tabla hash, dejando todas las posiciones impares vacías. 
Por esta razón, a menudo se elige un tamaño de tabla hash que sea un número primo.
       """