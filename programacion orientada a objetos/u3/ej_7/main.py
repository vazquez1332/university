from manejador import ManejaPersonal
from clase_menu import Menu
from ObjectEncoder import ObjectEncoder

if __name__ == "__main__":
    manejador = ManejaPersonal()
    
    jsonF = ObjectEncoder()   #Manejador JSON
      
    diccionario=jsonF.leerJSONArchivo('personal.json') #Lee archivo y lo transforma en diccionario
    jsonF.decodificarDiccionario(diccionario, manejador)
    #Menu
    menu = Menu(8)
    opciones = ["Insertar personal en posición", "Agregar personal", "Dada una posición mostrar tipo de dato", "Ingresa nombre carrera y dar lista ordenada de todos los agentes que son docentes investigadores", "Dada un area, contar los agentes docente investigador y los investigadores", "Generar listado ordenado por apellido de todos los agentes", "Dada una categoría de investigacion listar apellido nombre e importe de todos los docentes investigadores, realizar total de importe extra", "Almacena datos en personal.json"]
    
    menu.IngresaOpcion(opciones)
    menu.Muestra()
    
    op = int(input("Ingrese opcion: "))
    while op != menu.getCantidad() + 1:
        if op == 1:
            elemento = manejador.CreaElemento()
            if elemento != -1:
                
                posicion = int(input("Ingrese posicion a colocar elemento: "))
                manejador.insertarElemento(posicion, elemento)
            else:
                print("No se creo el elemento ")
        elif op == 2:
            elemento = manejador.CreaElemento()
            if elemento != -1:    
                manejador.agregarElemento(elemento)
            else:
                print("No se creo el elemento ")
           
        elif op == 3:
            pos = int(input("Ingrese posicion a ver: "))
            manejador.MostrarElemento(pos)          
        elif op == 4:
            carrera = input("Ingrese nombre de carrera a filtrar: ")      
            manejador.listaOrdenadaNombre(carrera)
            
        elif op == 5:
            area = input("Ingrese area de investigacion: ")
            manejador.cuentaPorArea(area)
        elif op == 6:
           manejador.ordenaPorApellido()
           manejador.Muestra()
        elif op == 7:             
            cat = input("Ingrese categoria: ")
            manejador.listaPorCat(cat)
        elif op == 8:
            # Guardar datos de lista en objeto
            d = manejador.toJSON()
            jsonF.guardarJSONArchivo(d, "personal.json")
        else:
            print("Ingreso opcion incorrecta ")
            
        menu.Muestra()
        op = int(input("Ingrese opcion: "))