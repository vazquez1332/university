"""El archivo atenciones registra: DNI, fecha de atención en formato (dd/mes/año), importe de
atención, entidad prestadora y el porcentaje de cobertura que tiene el afiliado."""

class Atencion:
    __dni:str
    __fecha:str
    __importe:float
    __entidad:str
    __porcentaje:int

    def __init__(self, fila:list[str]) -> None:
        self.__dni=fila[0]
        self.__fecha=fila[1]
        self.__importe=float(fila[2])
        self.__entidad=fila[3]
        self.__porcentaje=int(fila[4])

    def __str__(self) -> str:
        return f"{self.__dni, self.__entidad, self.__fecha, self.__importe, self.__porcentaje}"
    
    def getDni(self) -> str:
        return self.__dni
    
    def getFecha(self) -> str:
        return self.__fecha
    
    def getImporte(self) -> str:
        return self.__importe
    
    def getEntidad(self) -> str:
        return self.__entidad
    
    def getPorcentaje(self) -> int:
        return self.__porcentaje
