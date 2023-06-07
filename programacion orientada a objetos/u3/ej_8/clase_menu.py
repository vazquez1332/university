class Menu:

    def __init__(self, cantidad):
        self.__lista = []
        self.__cantidad = cantidad

    def getCantidad(self):
        return int(self.__cantidad)
    
    def IngresaOpcion(self, opciones):
        for i in range(self.__cantidad):
            self.__lista.append(opciones[i])
            
    def Muestra (self):
        i = 1
        for opcion in self.__lista:
            print(f"{i} {opcion}")
            i = i + 1
        print (f"{i} Salir ")

    
            



