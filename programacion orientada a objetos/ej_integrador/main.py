from manejadorAlumno import Manejador_Alumno
from manejadorMateria import Manejador_Materia
from claseMenu import Menu

if __name__=="__main__":
    arreglo=Manejador_Alumno.inicializar()
    manejadorAlumno=Manejador_Alumno(arreglo)
    #print("\n")
    lista=Manejador_Materia.inicializar()
    manejadorMateria=Manejador_Materia(lista)
    
    Menu(manejadorMateria,manejadorAlumno)
    
 
