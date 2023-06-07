class Sabor:
    __id: int
    __ingredientes: str
    __nombre: str

    def __init__(self, fila: list[str]) -> None:
        self.__id = int(fila[0])
        self.__ingredientes = fila[1]
        self.__nombre = fila[2]

    def __str__(self) -> str:
        return f"Sabor: {self.__nombre}, ID: {self.__id}"
    
    def getId(self) -> int:
        return self.__id
    
    def getNombre(self) -> str:
        return self.__nombre
    
