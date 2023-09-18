from nodo import Nodo

class Arbol:
    __raiz: Nodo or None
    __cant: int

    def __init__(self):
        self.__raiz = None
        self.__cant = 0

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

    def mostrar(self, nodo, nivel=0):
        if nodo is not None:
            self.mostrar(nodo.getDer(), nivel + 1)
            print(" " * 4 * nivel + "->", nodo.getDato())
            self.mostrar(nodo.getIzq(), nivel + 1)

if __name__ == "__main__":

    arbol = Arbol()

    try:
        datos = [20, 10, 30, 5, 15, 25, 35]
        for dado in datos:
            arbol.insertar(dado)

        arbol.mostrar(arbol.getRaiz())

    except Exception as e:
        print(str(e))
 
