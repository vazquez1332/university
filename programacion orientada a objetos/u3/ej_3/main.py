from manejadorInscripcion import ManejadorInscripcion
from manejadorPersona import ManejadorPersona
from manejadorTaller import ManejadorTaller
from menu import Menu

if __name__=="__main__":
    manejador_taller = ManejadorTaller()
    manejador_persona = ManejadorPersona()
    manejador_inscripcion = ManejadorInscripcion()

    Menu(manejador_inscripcion, manejador_persona, manejador_taller)

    