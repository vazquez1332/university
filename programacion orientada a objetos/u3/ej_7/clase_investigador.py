from clase_personal import Personal

class Investigador(Personal):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion)
        self.__area = area_investigacion
        self.__tipo = tipo_investigacion
        
    def getArea_investigacion(self):
        return self.__area
    
    def getTipo_investigacion(self):
        return self.__tipo
    
    def getSueldo(self):
        sueldo = float(super().getSueldo_basico()) + (float(super().getAntiguedad()))/100 * float(super().getSueldo_basico())
        return sueldo
    def __str__(self):
        cadena = str(super().getCuil()) + " "
        cadena += super().getApellido() + " "
        cadena += str(self.getSueldo()) + " "
        return cadena

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = super().getCuil(),
                apellido = super().getApellido(),
                nombre = super().getNombre(),
                sueldo_basico = super().getSueldo_basico(),
                antiguedad = super().getAntiguedad(),
                carrera = super().getCarrera(),
                cargo = super().getCargo(),
                catedra = super().getCatedra(),
                area_investigacion = self.__area,
                tipo_investigacion = self.__tipo,
                )
            )
        return d

