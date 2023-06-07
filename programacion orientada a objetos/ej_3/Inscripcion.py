from Persona import Persona
from Taller import TallerCapacitacion

class Inscripcion:
    __fecha: str
    __pago: bool = False
    __persona: Persona
    __taller: TallerCapacitacion

    def __init__(self, fecha: str, persona: Persona, taller: TallerCapacitacion) -> None:
        self.__fecha = fecha
        self.__persona = persona
        self.__taller = taller

    def __str__(self) -> str:
        return f"{self.__fecha, self.__pago, self.__persona, self.__taller}"
    
    def getPersona(self) -> Persona:
        return self.__persona
    
    def getTaller(self) -> TallerCapacitacion:
        return self.__taller
    
    def getFecha(self) -> str:
        return self.__fecha
    
    def getPago(self) -> bool:
        return self.__pago
    
    def setPago(self) -> None:
        self.__pago = not self.__pago

    

 