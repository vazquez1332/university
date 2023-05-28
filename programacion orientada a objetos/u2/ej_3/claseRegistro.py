class Registro: 
    __temperatura: float
    __humedad: float
    __presion: float

    def __init__(self, v1:float, v2:float, v3: float):
        self.__temperatura=v1
        self.__humedad=v2
        self.__presion=v3
    
    def __repr__(self)->str:
        return f"{self.__temperatura, self.__humedad, self.__presion}"

    def getTemperatura(self)->float:
        return self.__temperatura
    
    def getHumedad(self)->float:
        return self.__humedad
    
    def getPresion(self)->float:
        return self.__presion
    


    