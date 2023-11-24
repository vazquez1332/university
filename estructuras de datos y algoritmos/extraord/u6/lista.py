
class Nodo:
    __dato = None
    __siguiente = None

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    
    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__dato = dato
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
class lista:
    __cabeza = None
    __cantidad: int
    
    def __init__ (self):
        self.__cabeza 
        self.__cantidad = 0
    
    def vacio(self):
        return self.__cabeza == None
 
    def buscar(self, dato):
        aux = self.__cabeza
        
        while aux != None and aux.getDato() != dato:
            aux = aux.getSiguiente()
        
        if aux == None:
            return -1
        else:
            return aux

    def insertarLista(self, dato):
        nuevo = Nodo(dato)
        if self.vacio() or dato < self.__cabeza.getDato(): #type: ignore
            nuevo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            anterior = None
            
            while aux is not None and dato > aux.getDato():
                anterior = aux
                aux = aux.getSiguiente()

            nuevo.setSiguiente(aux)
            anterior.setSiguiente(nuevo) #type: ignore
        self.__cantidad += 1
    
    def eliminar(self, dato):
        aux = self.__cabeza
        anterior = None

        while aux != None and aux.getDato() != dato:
            anterior = aux
            aux = aux.getSiguiente()
        
        if aux == None:
            print("El dato no existe")
        elif anterior == None:
            self.__cabeza = aux.getSiguiente() 
        else:
            anterior.setSiguiente(aux.getSiguiente())

    def mostrarLista(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()