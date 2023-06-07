class Carrera:
    __codigo: int
    __nombre: str
    __duracion: str
    __titulo: str

    def __init__(self, fila: list[str]) -> None:
        self.__codigo = int(fila[1])
        self.__nombre = fila[2]
        self.__duracion = fila[3]
        self.__titulo = fila[4]

    def __str__(self) -> str:
        return f"Carrera: {self.__codigo, self.__nombre, self.__duracion, self.__titulo}"

    def getNombre(self) -> str:
        return self.__nombre
    
    def getDuracion(self) -> str:
        return self.__duracion
    
    def getCodigo(self) -> int:
        return self.__codigo
