from Empleado import Empleado

class Externo(Empleado):
    __tarea: str
    __fecha_inicio: str
    __fecha_finalizacion: str
    __viatico: float
    __costo: float
    __seguro: float

    def __init__(self, fila: list[str]) -> None:
        super().__init__(fila[0], fila[1], fila[2], fila[3])
        self.__tarea = fila[4]
        self.__fecha_inicio = fila[5]
        self.__fecha_finalizacion = fila[6]
        self.__viatico = float(fila[7])
        self.__costo = float(fila[8])
        self.__seguro = float(fila[9])

    def getTarea(self) -> str:
        return self.__tarea
    
    def getFechaFin(self) -> str:
        return self.__fecha_finalizacion
    
    def getCosto(self) -> float:
        return self.__costo

    def calculaSueldo(self) -> None:
        sueldo = self.__costo - self.__viatico - self.__seguro
        return super().setSueldo(sueldo)
    