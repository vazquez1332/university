from Empleado import Empleado

class Contratado(Empleado):
    __fecha_inicio: str
    __fecha_finalizacion: str
    __cant_hora: int
    __valor_hora: float


    def __init__(self, fila: list[str]) -> None:
        super().__init__(fila[0], fila[1], fila[2], fila[3])
        self.__fecha_inicio = fila[4]
        self.__fecha_finalizacion = fila[5]
        self.__cant_hora = int(fila[6])
        self.__valor_hora = float(fila[7])

    def addHoras(self, horas: int) -> None:
        self.__cant_hora += horas
        print("Horas sumadas")
    
    def calculaSueldo(self) -> None:
        sueldo = self.__cant_hora * self.__valor_hora
        return super().setSueldo(sueldo)