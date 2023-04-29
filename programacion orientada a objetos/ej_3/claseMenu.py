from claseRegistro import Registro
from numpy import ndarray

class Menu:
    __opcion: int
    __array: ndarray

    def __init__(self, opcion: int, array:ndarray):
        self.__opcion=opcion
        self.__array=array
        self.__procesarOpcion()

    @staticmethod
    def mostrarOpciones()->None:
        print("------MENU DE OPCIONES------\n")
        print("Opcion 1: Mostrar para cada variable el día y hora de menor y mayor valor.\n")
        print("Opcion 2: Indicar la temperatura promedio mensual por cada hora.\n")
        print("Opcion 3: Dado un número de día listar los valores de las tres variables para cada hora del día dado.\n")
        print("Opcion 0: Para finalizar.\n")
                
    def __procesarOpcion(self)->None:
            if self.__opcion == 1: 
                self.__mostrarMayorMenor()
            elif self.__opcion == 2: 
                self.__promedioMensual()
            elif self.__opcion == 3: 
                self.__listarVariables(int(input("Ingrese el dia: \n")))

    def __mostrarMayorMenor(self)->None:
        tuplaMayor=[(-1,-1),(-1,-1),(-1,-1)]
        tuplaMenor=[(-1,-1),(-1,-1),(-1,-1)]
        self.__buscaMayor(tuplaMayor)
        self.__buscaMenor(tuplaMenor)
        variables=["temperatura","humedad","presion"]
        i=0
        for i in range(len(variables)):
            print(f"Variable: {variables[i]}\n")
            print(f"Mayor, dia: {tuplaMayor[i][0]} y hora: {tuplaMayor[i][1]}:00\n")
            print(f"Menor, dia: {tuplaMenor[i][0]} y hora: {tuplaMenor[i][1]}:00\n")
            print("\n")

    def __buscaMayor(self, lista:list[tuple])->None:
        max1=float("-inf")
        max2=float("-inf")
        max3=float("-inf")
        for dia in range(len(self.__array)):
            for hora in range(len(self.__array[dia])):
                temp=self.__array[dia,hora].getTemperatura()
                hum=self.__array[dia,hora].getHumedad()
                pres=self.__array[dia,hora].getPresion()
                if temp>max1:
                    max1=temp
                    lista[0]=(dia+1,hora)
                if hum>max2:
                    max2=hum
                    lista[1]=(dia+1,hora)
                if pres>max3:
                    max3=pres
                    lista[2]=(dia+1,hora)
        
    def __buscaMenor(self, lista:list[tuple])->None:
        min1=float("inf")
        min2=float("inf")
        min3=float("inf")
        for dia in range(len(self.__array)):
            for hora in range(len(self.__array[dia])):
                temp=self.__array[dia,hora].getTemperatura()
                hum=self.__array[dia,hora].getHumedad()
                pres=self.__array[dia,hora].getPresion()
                if temp<min1:
                    min1=temp
                    lista[0]=(dia+1,hora)
                if hum<min2:
                    min2=hum
                    lista[1]=(dia+1,hora)
                if pres<min3:
                    min3=pres
                    lista[2]=(dia+1,hora)

    def __promedioMensual(self)->None:
        temperaturas=[]
        for hora in range(24):
            acum=0
            for dia in range(len(self.__array)):
                acum+=self.__array[dia,hora].getTemperatura()
            temperaturas.append(acum/len(self.__array))  
        for hora in range(len(temperaturas)):
            print("La temperatura promedio mensual para la hora %d:00, es: %.2f\n"%(hora,temperaturas[hora]))

    def __listarVariables(self, dia:int)->None:
        variables=[]
        for hora in range(24):
            variables.append(
                Registro(
                    self.__array[dia-1, hora].getTemperatura(),
                    self.__array[dia-1, hora].getHumedad(),
                    self.__array[dia-1, hora].getPresion()
                )
            )
            print(f"Dia: {dia}, hora: {hora}:00\n -Temperatura: {variables[hora].getTemperatura()}\n -Humedad: {variables[hora].getHumedad()}\n -Presión atmosférica: {variables[hora].getPresion()}\n")
