from atenciones import Atencion
from manejadorAfiliados import ManejadorAfiliado
import csv

class ManejadorAtenciones:
    __atenciones: list[Atencion]
    __manejadorAfiliados: ManejadorAfiliado

    def __init__(self, path:str, manejador: ManejadorAfiliado) -> None:
        self.__carga(path)
        self.__manejadorAfiliados=manejador

    def __carga(self, path:str):
        with open(path, "r") as file:
            reader=csv.reader(file, delimiter=";")
            next(reader,None)
            self.__atenciones=[Atencion(fila) for fila in reader]

        for fila in self.__atenciones:
            print(f"{fila}")

    def buscarAtencion(self, fecha:str, entidad:str) -> None:
        total=0
        print(f"Atenciones  Fecha:{fecha}")
        print()
        print("DNI      Nombre afiliado     Importe")
        for atencion in self.__atenciones:
            if atencion.getFecha() == fecha and atencion.getEntidad()==entidad:
                nombre=self.__manejadorAfiliados.obtenerNombre(atencion.getDni())
                print(f"{atencion.getDni()}   {nombre}  {atencion.getImporte()}")

                porcentaje=atencion.getPorcentaje()
                total+=atencion.getImporte()

        print()
        print(f"                         Total:{(total*porcentaje)/100}")
                
    def buscarporDNI(self, dni:str) -> None:
        cont=0
        nombre=self.__manejadorAfiliados.obtenerNombre(dni)
        print()
        print(f"Afiliado: {nombre}")
        for atencion in self.__atenciones:
            if atencion.getDni() == dni:
                cont+=1
        print(f"Cantidad de atenciones: {cont}")

    def sinAtenciones(self) -> None:
        dnis=self.__manejadorAfiliados.getDNIS()
        i=0
        lista=[]
        print()
        print("Afiliados sin atencion: ")
        for dni in dnis:
            if dni != self.__atenciones[i].getDni():
                i+=1
            else:
                lista.append(dni)
                i+=1
        
        for dni in lista:
            print(f"{self.__manejadorAfiliados.obtenerNombre(dni)}")
