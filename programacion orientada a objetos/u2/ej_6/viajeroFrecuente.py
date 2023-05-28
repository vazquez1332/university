class ViajeroFrecuente:
    __num_viajero:int
    __dni:str
    __nombre:str
    __apellido:str
    __millas_acum:int

    def __init__(self, v1:str, v2:str, v3:str, v4:str, v5: str):
        self.__num_viajero=int(v1)
        self.__dni=v2
        self.__nombre=v3
        self.__apellido=v4
        self.__millas_acum=int(v5)

    def __gt__(self, otro:"ViajeroFrecuente")->bool:
        return self.__millas_acum > otro.__millas_acum
    
    def __add__(self, millas:int)->"ViajeroFrecuente":
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido,self.__millas_acum+millas)
    
    def __sub__(self, canje:int)->"ViajeroFrecuente":
        if self.__millas_acum>=canje:
            return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido,self.__millas_acum-canje)
        else: print("Canje invalido.")

    def __repr__(self)->str:
        return f"{self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum}"
    
    def get_millas_acum(self)->int:
        return self.__millas_acum

    
    
    

    
    


            