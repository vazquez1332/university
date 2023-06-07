class Persona:
    __nombre: str
    __direccion: str
    __dni: str

    def __init__(self, nombre: str, direccion: str, dni: str) -> None:
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni

    def __str__(self) -> str:
        return f"{self.__nombre, self.__direccion, self.__direccion}"
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getDireccion(self) -> str:
        return self.__direccion
    
    def getDni(self) -> str:
        return self.__dni
    