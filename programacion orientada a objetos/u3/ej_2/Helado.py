from Sabor import Sabor

class Helado: 
    __gramos: float
    __precio: float
    __sabores : list[Sabor]

    def __init__(self, g: float, p: float) -> None:
        self.__gramos = g
        self.__precio = p
        self.__sabores = []

    def setSabor(self, sabor: Sabor) -> None:
        self.__sabores.append(sabor)

    def __str__(self) -> str:
        return f"""HELADO
        peso: {self.__gramos}
        precio: {self.__precio}
        sabores: {self.__sabores}
        """

    