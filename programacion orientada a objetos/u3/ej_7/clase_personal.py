class Personal:
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera = " ", cargo = " ", catedra = " ", area_investigacion = " ", tipo_investigacion = " "):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo_basico = sueldo_basico
        self.__antiguedad = antiguedad
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
        self.__area_investigacion = area_investigacion
        self.__tipo_investigacion = tipo_investigacion

    def __str__(self):
        cadena = str(self.__cuil) + " "
        cadena += self.__nombre
        return cadena

    def getCuil(self):
        return str(self.__cuil)
    
    def getApellido(self):
        return self.__apellido
    
    def getCategoria(self):
        pass
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldo_basico(self):
        return self.__sueldo_basico
    
    def getAntiguedad(self):
        return self.__antiguedad

    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra
    
    def getArea_investigacion(self):
        return str(self.__area_investigacion)
    
    def getTipo_investigacion(self):
        return self.__tipo_investigacion
    
    def __lt__(self, otro):
        return self.__nombre > otro.__nombre