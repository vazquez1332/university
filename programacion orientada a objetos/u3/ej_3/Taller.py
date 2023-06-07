class TallerCapacitacion:
    __id: int 
    __nombre: str
    __vacantes: int 
    __monto: int

    def __init__(self, fila: list[str]) -> None:
        self.__id = int(fila[0])
        self.__nombre = fila[1]
        self.__vacantes = int(fila[2])
        self.__monto = int(fila[3])

    def __str__(self) -> str:
        return f"{self.__id, self.__nombre, self.__vacantes, self.__monto}"
    
    def getId(self) -> int:
        return self.__id
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getVacantes(self) -> int:
        return self.__vacantes
    
    def getMonto(self) -> int:
        return self.__monto
    
    def setVacantes(self) -> None:
        self.__vacantes -= 1
    