from manejador import ManejaAutos
from ObjectEncoder import ObjectEncoder
from clase_usado import VehiculoUsado
from clase_nuevo import Vehiculonuevo
from clase_menu import Menu

if __name__ == "__main__":
    jsonF = ObjectEncoder()   #Manejador JSON
    manejador = ManejaAutos() #Lista enlazada autos
    
    # Leer datos del archivo JSON 
    
    diccionario=jsonF.leerJSONArchivo('vehiculos.json')
    vehiculos=jsonF.decodificarDiccionario(diccionario, manejador)
    
    #Menu
    menu = Menu(7)
    opciones = ["Insertar en posición", "Agregar vehiculo", "Dada una posición mostrar tipo de dato", "Dada la patente de usado, modifica", "mostrar todos los datos del más económico", "Mostrar todos", "Almacenar objetos en archivo"]
    menu.IngresaOpcion(opciones)
    menu.Muestra()
    op = int(input("Ingrese opcion: "))
    while op != menu.getCantidad() + 1:
        if op == 1:
            #Agrega vehiculo en la posición determinada
            pos = int(input("Ingrese posición en la lista para colocar el vehículo: "))
            eleccion = int(input("Ingrese un auto 1-viejo 2-nuevo: "))
            modelo = input("Ingrese modelo: ")
            cantPuertas = input("Ingrese cantPuertas: ")
            color = input("Ingrese color: ")
            precioVenta = input("Ingrese precio: ")
            marca = input("Ingrese marca: ")
            if eleccion == 1:
                patente = input("Ingrese patente: ") 
                anio = input("Ingrese anio: ")
                kilometraje = input("Ingrese kilometraje: ")
                vehiculo = VehiculoUsado(modelo,cantPuertas,color,precioVenta,marca,patente,anio,kilometraje)            
            elif eleccion == 2:
                version = input("Ingrese version: ")
                vehiculo = Vehiculonuevo(modelo,cantPuertas,color,precioVenta,marca,version)
            manejador.agregaAutoPorPos(pos, vehiculo)
        elif op == 2:
            #Agrega vehiculo en la coleccion
            eleccion = int(input("Ingrese un auto 1-viejo 2-nuevo: "))
            modelo = input("Ingrese modelo: ")
            cantPuertas = input("Ingrese cantPuertas: ")
            color = input("Ingrese color: ")
            precioVenta = input("Ingrese precio: ")
            marca = input("Ingrese marca: ")
            if eleccion == 1:
                patente = input("Ingrese patente: ") 
                anio = input("Ingrese anio: ")
                kilometraje = input("Ingrese kilometraje: ")
                vehiculo = VehiculoUsado(modelo,cantPuertas,color,precioVenta,marca,patente,anio,kilometraje)
                manejador.agregarAuto(vehiculo)            
            elif eleccion == 2:
                version = input("Ingrese version: ")
                vehiculo = Vehiculonuevo(modelo,cantPuertas,color,precioVenta,marca,version)
                manejador.agregarAuto(vehiculo)
        elif op == 3:
            pos = int(input("Ingrese posicion a mostrar: "))
            manejador.MuestraPorPos(pos)
        elif op == 4:
            patente = input("Ingrese patente a buscar: ")
            manejador.BuscaPorPatente(patente)
        elif op == 5:
            manejador.BuscaMenor()
        elif op == 6:
            manejador.Muestra()
        elif op == 7:             
            # Guardar datos de lista en objeto
            d = manejador.toJSON()
            jsonF.guardarJSONArchivo(d, "vehiculos.json")
        else:
            print("Ingreso opcion incorrecta ")
            
        menu.Muestra()
        op = int(input("Ingrese opcion: "))
            
    
        

        

   
    