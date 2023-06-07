from zope.interface import Interface

class Imanejador(Interface):
    
    def insertarElemento(self, posicion, elemento):
        pass
    
    def agregarElemento(self, elemento):
        pass
    
    def mostrarElemento(self, posicion):
        pass
