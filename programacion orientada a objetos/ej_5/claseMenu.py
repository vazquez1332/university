from clasePlanAhorro import PlanAhorro
from typing import List

class Menu:
    __planes:List[PlanAhorro]
    __switcher:dict

    def __init__(self, lista:List[PlanAhorro])->None:
        self.__planes=lista
        self.__switcher={
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            0: self.salir
        }
        self.procesarMenu()

    def procesarMenu(self)->None:
        while True:
            self.__printMenu()
            opcion = int(input("\nIngrese la opción deseada: "))
            if opcion in self.__switcher:
                self.__switcher[opcion]()
            else:
                print("\nOpción inválida")

    def __printMenu(self)->None:
        print("\nMenú de opciones:")
        print("1. Actualizar valor del vehículo de cada plan.")
        print("2. Mostrar planes con cuota inferior a un valor.")
        print("3. Mostrar monto para licitar.")
        print("4. Modificar la cantidad de cuotas que debe tener pagas para licitar.")
        print("0. Salir.")

    def opcion1(self)->None:
        for plan in self.__planes:
            print(f"Codigo de plan: {plan.getCodigo()}\nModelo: {plan.getModelo()}\nVersion: {plan.getVersion()}\n")
            plan.setValor(int(input("Ingrese el nuevo valor del vehiculo: ")))

    def opcion2(self)->None:
        valor=int(input("Ingrese el valor: "))
        for plan in self.__planes:
            if plan.importeCuota()<valor:
                print(plan)
            else: print("No existe ningun plan.")
    
    def opcion3(self)->None:
        for plan in self.__planes:
            print(f"Plan:{plan}\nMonto para licitar: {plan.montoLicitar()}")

    def opcion4(self)->None:
        i=0
        codigo=int(input("Ingrese el codigo de plan: "))
        while i<len(self.__planes) and self.__planes[i].getCodigo()!=codigo:
            i+=1
        if i<len(self.__planes):
            self.__planes[i].modificarCuotas(input("Ingrese la nueva cantidad de cuotas: "))
            print("\nCambio realizado con exito.")
        else: print("\nCodigo no encontrado.")

    def salir(self)->None:
        exit()
