import abc
from abc import ABC

class Empleado(ABC):
    __dni: str
    __nombre: str
    __direccion: str
    __telefono: str
    __sueldo: float

    def __init__(self, dni: str, nombre: str, direccion: str, telefono: str) -> None:
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    @abc.abstractmethod
    def calculaSueldo(self) -> None:
        pass

    def setSueldo(self, sueldo: float) -> None:
        self.__sueldo = sueldo
    
    def getDni(self) -> str:
        return self.__dni
    

