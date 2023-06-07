from Empleado import Empleado

class Planta(Empleado):
    __sueldo_basico: float
    __antiguedad: int

    def __init__(self, fila: list[str]) -> None:
        super().__init__(fila[0], fila[1], fila[2], fila[3])
        self.__sueldo_basico = float(fila[4])
        self.__antiguedad = int(fila[5])

        sueldo = (self.__sueldo_basico * 0.01) * self.__antiguedad
        super().setSueldo(sueldo + self.__sueldo_basico)

    def calculaSueldo(self) -> None:
        sueldo = (self.__sueldo_basico * 0.01) * self.__antiguedad
        return super().setSueldo(sueldo + self.__sueldo_basico)
