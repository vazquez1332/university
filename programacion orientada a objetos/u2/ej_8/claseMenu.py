from claseConjunto import Conjunto

class Menu:
    __opcion:int
    __switcher:dict
    __conjunto1:"Conjunto"
    __conjunto2:"Conjunto"
    def __init__(self, opcion:int, conjunto1:"Conjunto", conjunto2:"Conjunto")->None:
        self.__opcion=opcion
        self.__conjunto1=conjunto1
        self.__conjunto2=conjunto2
        self.__switcher={
            1:self.__opcion1,
            2:self.__opcion2,
            3:self.__opcion3,
        }
        self.__procesarOpcion()

    @staticmethod
    def mostrarMenu()->None:
        print("1. Unión de dos conjuntos")
        print("2. Diferencia de dos conjuntos")
        print("3. Verificar si dos conjuntos son iguales")
        print("0. Salir")

    def __procesarOpcion(self)->None:
        if self.__opcion in self.__switcher:
            self.__switcher[self.__opcion]()
        else: print("Opcion invalida. ")

    def __opcion1(self)->None:
        conjuntoresult=self.__conjunto1+self.__conjunto2
        print(f"Resultado de la union: {conjuntoresult}")

    def __opcion2(self)->None:
        conjuntoresult=self.__conjunto1-self.__conjunto2
        print(f"Resultado de la interseccion: {conjuntoresult}")

    def __opcion3(self)->None:
        if self.__conjunto1 == self.__conjunto2:
            print("Los conjuntos son iguales. ")
        else: print("Los conjuntos son distintos. ")