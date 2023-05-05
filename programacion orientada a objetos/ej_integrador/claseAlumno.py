class Alumno:
    __dni:str
    __apellido:str
    __nombre:str
    __carrera:str
    __año:int

    def __init__(self, v1:str, v2:str, v3:str, v4:str, v5:str)->None:
        self.__dni=v1
        self.__apellido=v2
        self.__nombre=v3
        self.__carrera=v4
        self.__año=int(v5)

    def __str__(self)->str:
        return f"{self.__dni, self.__apellido, self.__nombre, self.__carrera, self.__año}"
    
    def getDni(self)->str:
        return self.__dni
    
    def getNombrecompleto(self)->str:
        return f"{self.__apellido} {self.__nombre}"
    
    def getAño(self)->int:
        return self.__año
    
    def __lt__(self, otro: "Alumno")->bool:
        retorno=False
        if self.__año<otro.__año:
            retorno=not retorno
        elif self.__año==otro.__año:
            if self.__apellido<otro.__apellido:
                retorno=not retorno
            elif self.__apellido==otro.__apellido:
                return self.__nombre<otro.__nombre
        return retorno



    
