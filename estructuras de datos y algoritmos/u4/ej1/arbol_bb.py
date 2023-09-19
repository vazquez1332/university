from nodo import Nodo

class Arbol:
    __raiz: Nodo or None

    def __init__(self):
        self.__raiz = None

    def getRaiz(self):
        return self.__raiz
 
    def insertar(self, dato, nodo=None):
        if nodo is None:
            if self.__raiz is None:
                self.__raiz = Nodo(dato)
            else:
                self.insertar(dato, self.__raiz)

        elif nodo.getDato() == dato:
                raise Exception("Dato ya existente.")
        
        else:
            if dato < nodo.getDato():
                if nodo.getIzq() is None:
                    nodo.setIzq(Nodo(dato))
                else:
                    self.insertar(dato, nodo.getIzq())

            else:
                if nodo.getDer() is None:
                    nodo.setDer(Nodo(dato))
                else:
                    self.insertar(dato, nodo.getDer())

    def mostrar(self, nodo, nivel = 0):
        if nodo is not None:
            self.mostrar(nodo.getDer(), nivel + 1)
            print(" " * 4 * nivel + "->", nodo.getDato())
            self.mostrar(nodo.getIzq(), nivel + 1)


