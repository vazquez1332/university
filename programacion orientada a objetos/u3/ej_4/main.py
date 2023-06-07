from manejadorEmpleado import ManejadorEmpleado

def menu():
    print("\n------MENU------")
    print("1- Registrar horas")
    print("2- Total de tarea")
#    print("3- Ayuda economica")
#    print("4- Calcular sueldo")
    print("0- Para salir")

if __name__=="__main__":
    manejador = ManejadorEmpleado(int(input("Ingrese el tamaño del arreglo: ")))
    
    menu()
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 0:
        if opcion == 1:
            manejador.registrarHoras(input("Ingrese el dni: "), int(input("Ingrese la cantidad de horas: ")))
        elif opcion == 2:
            manejador.buscarTarea(input("Ingrese la tarea a buscar: "))
        else:
            print("Opcion incorrecta, reingrese")
        menu()
        opcion = int(input("Ingrese una opcion: "))