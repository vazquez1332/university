from Carrera import Carrera

class Facultad: 
    __codigo: int
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: str
    __carreras: list[Carrera]

    def __init__(self, fila: list[str]) -> None:
        self.__codigo = int(fila[0])
        self.__nombre = fila[1]
        self.__direccion = fila[2]
        self.__localidad = fila[3]
        self.__telefono = fila[4]
        self.__carreras = []

    def setCarrera(self, fila: list[str]) -> None:
        self.__carreras.append(Carrera(fila))

    def __str__(self) -> str:
        return f"{self.__codigo, self.__nombre, self.__direccion, self.__localidad, self.__telefono}"
    
    def getCarreras(self) -> list[Carrera]:
        return self.__carreras
    
    def getCodigo(self) -> int:
        return self.__codigo
    
    def getNombre(self) -> str:
        return self.__nombre

    def getLocalidad(self) -> str:
        return self.__localidad
    
    


    