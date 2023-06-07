from clase_personal import Personal

class PersonalApoyo(Personal):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion)
        self.__categoria = categoria
        
    def getCategoria(self):
        return self.__categoria
    
    def setCategoria(self, cat):
        self.__categoria = cat
    
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
                area_investigacion = super().getArea_investigacion(),
                tipo_investigacion = super().getTipo_investigacion(),
                categoria = self.__categoria
                )
            )
        return d
    
    def __str__(self):
        cadena = str(super().getCuil()) + " "
        cadena += super().getApellido() + " "
        cadena += str(self.getSueldo()) + " "
        return cadena
    
    def getSueldo(self):
        if int(self.__categoria) > 20:
            categoria = 0.3
        elif int(self.__categoria) > 10:
            categoria = 0.2
        elif int(self.__categoria) > 0:
            categoria = 0.1
        else:
            categoria = 0
        sueldo = float(super().getSueldo_basico()) + (float(super().getAntiguedad()))/100 * float(super().getSueldo_basico()) + float(super().getSueldo_basico()) * categoria
        return sueldo