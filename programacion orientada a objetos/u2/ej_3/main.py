import csv
import numpy as np
from claseRegistro import Registro
from claseMenu import Menu

def test(arreglo)->None:
    #valores correctos
    menu_correcto=Menu(1, arreglo)
    assert menu_correcto is not None
    menu_correcto=Menu(2, arreglo)
    assert menu_correcto is not None
    menu_correcto=Menu(3, arreglo)
    assert menu_correcto is not None
    #valores incorrectos
    try:
        menu_incorrecto=Menu(5, arreglo)
        assert menu_incorrecto is None, "Error: Opcion fuera del rango\n"
    except AssertionError as e:
        print(e)

if __name__=="__main__":
    arreglo=np.empty((30,24), dtype=Registro)
    cabecera=True
    with open("archivo.csv","r") as file:
            reader=csv.reader(file, delimiter=",")
            for fila in reader:
                if cabecera:
                    cabecera=not cabecera
                else:
                    dia,hora,temp,hum,pres=map(float, fila)
                    arreglo[int(dia)-1, int(hora)-1]=Registro(temp, hum, pres)
    opcion = -1
    while opcion != 0:
        test(arreglo)
        Menu.mostrarOpciones()
        opcion=int(input("Ingrese la opcion: \n"))
        if opcion!=0:
            Menu(opcion, arreglo)


