class PlanAhorro:
    __codigoplan:int
    __modelo:str
    __version:str
    __valor:int
    __cuotasPlan:int=60
    __cuotasLicitar:int=10

    def __init__(self, codigo:int, modelo:str, version:str, valor:int)->None:
        self.__codigoplan=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor

    def __str__(self)->str:
        return f"{self.__codigoplan , self.__modelo, self.__version, self.__valor}"
    
    def getCodigo(self)->int:
        return self.__codigoplan
    
    def getModelo(self)->str:
        return self.__modelo
    
    def getVersion(self)->str:
        return self.__version
    
    def getValor(self)->int:
        return self.__valor
    
    @classmethod
    def getCuotasPlan(cls)->int:
        return cls.__cuotasPlan
    
    @classmethod
    def getCuotasPagas(cls)->int:
        return cls.__cuotasLicitar
    
    def importeCuota(self)->int:
        return(self.__valor/self.__cuotasPlan)+self.__valor*0.10
    
    def setValor(self, nuevovalor:int)->None:
        self.__valor=nuevovalor

    def montoLicitar(self)->int:
        return self.__cuotasLicitar*self.importeCuota()

    def modificarCuotas(self, cuotas:int)->None:
        self.__cuotasLicitar=cuotas

