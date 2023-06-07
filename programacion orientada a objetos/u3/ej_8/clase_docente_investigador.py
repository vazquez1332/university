from clase_docente import Docente
from clase_investigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_investigacion, importe_extra):
        super().__init__(cuil, apellido, nombre, sueldo_basico,antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion)
        self.__categoria_investigacion = categoria_investigacion 
        self.__importe_extra = importe_extra
    
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
                categoria_investigacion = self.__categoria_investigacion,
                importe_extra = self.__importe_extra
                )
            )
        return d
    
    def getImporteExtra(self):
        return self.__importe_extra
    
    def setImporte(self, imp):
        self.__importe_extra = imp
    def getSueldo(self):
        sueldo = super().getSueldo() + float(self.__importe_extra)
        return sueldo 
        
    def getCategoria(self):
        return self.__categoria_investigacion
        
    def __str__(self):
        cadena = str(super().getCuil()) + " "
        cadena += super().getApellido() + " "
        cadena += str(self.getSueldo()) + " "
        return cadena