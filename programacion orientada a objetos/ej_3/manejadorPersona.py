from Persona import Persona

class ManejadorPersona:
    __lista: list[Persona]

    def __init__(self) -> None:
        self.__lista = []
    
    def registarPersona(self) -> Persona:
        nombre = input("Ingrese nombre de la persona: ")
        direccion = input("Ingrese direccion: ")
        dni = input("Ingrese dni: ")
        
        persona = Persona(nombre, direccion, dni)
        self.__lista.append(persona)

        return persona
    
