from manejadorMateria import Manejador_Materia
from manejadorAlumno import Manejador_Alumno

class Menu:
    __manejadorMateria:"Manejador_Materia"
    __manejadorAlumno:"Manejador_Alumno"
    __switcher:dict

    def __init__(self, manejador1:"Manejador_Materia", manejador2:"Manejador_Alumno")->None:
        self.__manejadorMateria=manejador1
        self.__manejadorAlumno=manejador2
        self.__switcher={
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3
        }
        self.procesar_opcion()

    def procesar_opcion(self)->None:
        self.__mostrar_menu()
        opcion=int(input("\nIngrese la opcion: "))
        while opcion!=0:
            if opcion in self.__switcher:
                self.__switcher[opcion]()
            else: print("Opcion incorrecta. ")
            opcion=int(input("\nIngrese la opcion: "))

    def __mostrar_menu(self)->None:
        print("--------MENU--------")
        print("1: Buscar promedios. ")
        print("2: Informar estudiantes promocionales. ")
        print("3: Lista ordenada de alumnos. ")
        print("0: Finalizar. ")

    def opcion1(self)->None:
        dni=input("Ingrese el dni del alumno: ")
        self.__manejadorMateria.mostrar_promedio(dni)

    def opcion2(self)->None:
        lista=self.buscar_alumno(input("Ingrese el nombre de la materia: "))
        if lista:
            print("    DNI      Apellido y nombre          Fecha     Nota  Año que cursa ")
            print("--------- -------------------------   ----------  -----  ------------ ")
            for elemento in lista:
                print(f"{elemento[0]:<10} {elemento[1]:<25} {elemento[2]:<14} {elemento[3]:.2f}  {elemento[4]}")
        else: print("No hay ningun alumno promocional. ")

    def buscar_alumno(self, materia:str)->list[tuple[str, str, str, float, int]]:
        promocionales=[]
        lista1=self.__manejadorMateria.busca_promocional(materia)
        lista2=[]
        for catedra in lista1:
            lista2.append(catedra.getDni())
        for dni in lista2:
            seleccionado=self.__manejadorAlumno.busca_alumno(dni)
            for lista1 in lista1:
                dni=lista1.getDni()
                nombre=seleccionado.getNombrecompleto()
                fecha=lista1.getFecha()
                nota=float(lista1.getNota())
                año=int(seleccionado.getAño())
                promocionales.append((dni,nombre,fecha,nota,año))
        return promocionales

    
    def opcion3(self)->None:
        lista=self.__manejadorAlumno.ordenar()
        print("Lista ordenada: ")
        for elemento in lista:
            print(elemento)
        
    
        

    