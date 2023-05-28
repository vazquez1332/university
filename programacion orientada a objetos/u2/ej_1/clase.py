import re
class Email: 
    __id_cuenta: str 
    __dominio: str 
    __tipo_dominio: str 
    __contraseña: str 

    def __init__(self, v1:str, v2:str, v3:str, v4:str):
        self.__id_cuenta= v1
        self.__dominio= v2 
        self.__tipo_dominio= v3
        self.__contraseña= v4 

    def retornarMail(self)->str:
        return self.__id_cuenta + "@" + self.__dominio + "." + self.__tipo_dominio

    def getDominio(self)->str:
        return self.__dominio

    def crearCuenta(self, correo:str):
        id_correo=correo.split("@")
        self.__id_cuenta=id_correo[0]

        dominio_correo=id_correo[1].split(".")
        self.__dominio=dominio_correo[0]
        self.__tipo_dominio=dominio_correo[1]

        print("CUENTA CREADA CON EXITO")
        print(f"-Id Cuenta: {self.__id_cuenta}\n-Dominio: {self.__dominio}\n-Tipo de dominio: {self.__tipo_dominio}\n")

        return Email(self.__id_cuenta, self.__dominio, self.__tipo_dominio, "")
    
    def verificarContraseña(self, c:str)->bool:
        if self.__contraseña == c:
            print("Contraseña correcta.")
            return True
        else: print("Contraseña incorrecta.")
    
    def modificarContraseña(self, cnueva:str):
        self.__contraseña=cnueva
        return print("Su contraseña se ha cambiado con exito.\n")
    
    def __str__(self):
        return f"{self.__id_cuenta, self.__dominio, self.__tipo_dominio, self.__contraseña}"
    
    @staticmethod
    def cantDominios(dom:str, lista:list["Email"])->None:
        contador=0
        for lista in lista:
            if dom==lista.getDominio():
                contador+=1
        if contador==0: print("\nDominio no encontrado.")
        else: print("El dominio %s se encuentra en %d correo/s"%(dom,contador))