from clase_nodo import Nodo
from clase_vehiculo import Vehiculo

class ManejaAutos:
    __comienzo:Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    def agregarAuto(self, vehiculo):
        nodo = Nodo(vehiculo)
        if self.__comienzo == None:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            nodo.setSiguiente(None)
            aux.setSiguiente(nodo)
            self.__tope += 1
            
        
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            lista=[dato.toJSON() for dato in self]
            )
        return d

    def agregaAutoPorPos(self, pos, vehiculo):
        if pos == 1:
            self.agregarAuto(vehiculo)
        else:
            nodo = Nodo(vehiculo)
            aux = self.__comienzo
            for i in range(0, pos-1):
                prev = aux
                aux = aux.getSiguiente()
                
            prev.setSiguiente(nodo)
            nodo.setSiguiente(aux)
            
            self.__tope += 1
            
    def Muestra(self):
        for dato in self:
            print(dato)
    
    def MuestraPorPos(self, pos):
        for dato in self:
            if self.__indice == pos:
                print(dato.getClass())
                
    def BuscaPorPatente(self, patente):
        aux = self.__comienzo
        while aux != None and aux.getDato().getPatente() != patente:
            aux = aux.getSiguiente()
        if aux != None:
            precio = input("Ingrese nuevo precio del vehiculo: ")
            dato = aux.getDato()
            dato.setPrecio(precio)
        else:
            print("No se encontro el vehiculo ")
            
    def BuscaMenor(self):
        mini = Vehiculo("modelo", "cantPuertas", "color", 10000000000, "marca")
        for dato in self:
            if dato.importe() < mini.importe():
                mini = dato   
        print(mini)
                