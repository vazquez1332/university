from manejador import ManejaPersonal
from clase_menu import Menu
from ObjectEncoder import ObjectEncoder
from interfaceDirector import IDirector
from interfaceTesorero import ITesorero

if __name__ == "__main__":
    
    jsonF = ObjectEncoder()   #Manejador JSON

    usuario = input("Ingrese usuario: ")
    
    clave = input("Ingrese clave: ")
    
    if usuario == "tesorero" and clave == "uTesoreso/ag@74ck":
        maneja = (ITesorero(ManejaPersonal()))
        diccionario=jsonF.leerJSONArchivo('personal.json') #Lee archivo y lo transforma en diccionario
        jsonF.decodificarDiccionario(diccionario, maneja)
        opciones = ["Gastos sueldo por empleado"]
        menuTesorero = Menu(1)
        menuTesorero.IngresaOpcion(opciones)
        menuTesorero.Muestra()
        op = int(input("Ingrese opcion: "))
        while op != menuTesorero.getCantidad() + 1:
            if op == 1:
                cuil = input("Ingrese cuil a buscar: ")
                maneja.gastoSueldoPorEmpleado(cuil)
            else:
                print("Ingreso opcion incorrecta")
            menuTesorero.Muestra()
            op = int(input("Ingrese opcion: "))
    elif usuario == "director" and clave =="uDirector/ufC77#!1":
        maneja = (IDirector(ManejaPersonal()))
        diccionario=jsonF.leerJSONArchivo('personal.json') #Lee archivo y lo transforma en diccionario
        jsonF.decodificarDiccionario(diccionario, maneja)
        opciones = ["modificaBasico", "modifica cargo", "modifica Categoria", "Modifica importe"]
        menuDirector = Menu(4)
        menuDirector.IngresaOpcion(opciones)
        menuDirector.Muestra()
        op = int(input("Ingrese opcion: "))
        while op != menuDirector.getCantidad() + 1:
            if op == 1:
                cuil = input("Ingrese cuil a buscar: ")
                basico = int(input("Ingrese nuevo basico: "))
                maneja.modificarBasico(cuil, basico)
            elif op == 2:
                cuil = input("Ingrese cuil a buscar: ")
                cargo = int(input("Ingrese nuevo cargo: "))
                maneja.modificarPorcentajeporcargo(cuil,cargo)
            elif op == 3:
                cuil = input("Ingrese cuil a buscar: ")
                cat = int(input("Ingrese nueva categoria: "))
                maneja.modificarPorcentajeporcategoría(cuil,cat)
            elif op == 4:
                cuil = input("Ingrese cuil a buscar: ")
                importe = int(input("Ingrese nuevo importe: "))
                maneja.modificarImporteExtra(cuil, importe)
            
            else:
                print("Ingreso opcion incorrecta")
            menuDirector.Muestra()
            op = int(input("Ingrese opcion: "))
    else:
        print("Ingreso usuario o contraseña incorrecta")
        
    # Guardar datos de lista en objeto
    d = maneja.toJSON()
    jsonF.guardarJSONArchivo(d, "personal.json")