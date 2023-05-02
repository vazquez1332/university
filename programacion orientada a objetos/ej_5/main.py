from clasePlanAhorro import PlanAhorro
from claseMenu import Menu
import csv

"""def test()->None:
    lista_prueba=[
    PlanAhorro(1, "Modelo 1", "Versión 1", 100000),
    PlanAhorro(2, "Modelo 2", "Versión 2", 200000),
    PlanAhorro(3, "Modelo 3", "Versión 3", 300000)
    ]
    menu=Menu(lista_prueba)
     
    NOTA: Debido a la manera de implementar los metodos y clases no me es posible encontrar 
    una forma de realizar una funcion test() sin tener que ingresar valores por teclado. 
    Sugiero eliminar algunas filas del archivo planes.csv para probar todas las funciones 
    en menor tiempo.
    
    """

if __name__=="__main__":
    lista=[]
    with open("planes.csv","r") as planes:
        reader=csv.reader(planes, delimiter=";")
        for plan in reader:
            lista.append(PlanAhorro(
                int(plan[0]),plan[1],plan[2],int(plan[3])
            ))
    Menu(lista)