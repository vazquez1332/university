""""
El archivo de afiliados registra: DNI, nombre y apellido y la unidad en la que presta servicio
(FCEFyN, FASCO, etc.)
"""

class Afiliado:
    __dni:str
    __nombre:str
    __unidad:str

    def __init__(self, fila:list[str]) -> None:
        self.__dni=fila[0]
        self.__nombre=fila[1]
        self.__unidad=fila[2]

    def getDni(self) -> str:
        return self.__dni
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getUnidad(self) -> str:
        return self.__unidad
    
    def __str__(self) -> str:
        return f"{self.__dni, self.__nombre, self.__unidad}"
    
    def __lt__(self, other:"Afiliado") -> bool:
        retorno=False
        if self.__unidad < other.__unidad:
            retorno= not retorno
        elif self.__unidad == other.__unidad:
            if self.__nombre < other.__nombre:
                retorno= not retorno
        return retorno