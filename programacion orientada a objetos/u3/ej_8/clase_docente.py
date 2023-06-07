from clase_personal import Personal

class Docente(Personal):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    
    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra
        
    def __str__(self):
        cadena = str(super().getCuil()) + " "
        cadena += super().getApellido() + " "
        cadena += str(self.getSueldo()) + " "
        return cadena
    
    def getSueldo(self):
        if self.__cargo == "simple":
            cargo = 0.1
        elif self.__cargo == "semiexclusivo":
            cargo = 0.2
        elif self.__cargo == "exclusivo":
            cargo = 0.5
        else:
            cargo = 0   
        sueldo = float(super().getSueldo_basico()) + (float(super().getAntiguedad()))/100 * float(super().getSueldo_basico()) + float(super().getSueldo_basico()) * cargo
        return sueldo
    
    def toJSON(self):        
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = super().getCuil(),
                apellido = super().getApellido(),
                nombre = super().getNombre(),
                sueldo_basico = super().getSueldo_basico(),
                antiguedad = super().getAntiguedad(),
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra,
                area_investigacion = super().getArea_investigacion(),
                tipo_investigacion = super().getTipo_investigacion(),
                )
            )
        return d
