from manejador import ManejaAutos
from clase_nuevo import Vehiculonuevo
from ObjectEncoder import ObjectEncoder
import unittest

class Test(unittest.TestCase):
    def run(self):
        jsonF = ObjectEncoder()   #Manejador JSON
        manejador = ManejaAutos() #Lista enlazada autos
        # Leer datos del archivo JSON 
        diccionario=jsonF.leerJSONArchivo('vehiculos.json')
        jsonF.decodificarDiccionario(diccionario, manejador)
        """
        1. Insertar un vehículo en la colección en una posición determinada, 
        verificar el estado final de la lista. 
    
        Nota: se deben escribir test para verificar el estado de la lista, 
        cuando se inserta en la posición 0, 
        en una posición intermedia, y en la última posición. 
        """
        vehiculo = Vehiculonuevo("Aguile", 4, "Rojo", 100000, "Chevrolet", "Full")
        pos = 1
        manejador.agregaAutoPorPos(pos, vehiculo)
        manejador.Muestra()
        
        self.assertIn(vehiculo,manejador)
        print("\n \n")
        pos = 4
        manejador.agregaAutoPorPos(pos, vehiculo)
        
        self.assertIn(vehiculo,manejador)
        manejador.Muestra()
        print("\n \n")
        pos = manejador.getTope() + 1
        manejador.agregaAutoPorPos(pos, vehiculo)
        
        self.assertIn(vehiculo,manejador)
        manejador.Muestra()
        print("\n \n")
        
        """
        2. Agregar un vehículo a la colección, verificar el estado final de la lista.
        """
        manejador.agregarAuto(vehiculo)
        manejador.Muestra()
        print("\n \n")
        """
        3. Dada una posición de la Lista, obtener  un  objeto de la lista, verificar que el objeto es el que está en dicha posición.
        """
        pos = 5
        vehiculo = manejador.buscaPorPos(pos)
        print(vehiculo)
        manejador.MuestraPorPos(pos)
        
        self.assertEqual(vehiculo.getClass(), manejador.MuestraPorPos(pos))

        print("\n \n")
        
        """
        4. Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta, verificar el nuevo precio de venta.
        """
        
        vehiculo = manejador.BuscaPorPatente("eoeo", 400)
        self.assertEqual(vehiculo.importe(),348)

        print("\n \n")
        """
        # Guardar datos de lista en objeto
        d = manejador.toJSON()
        jsonF.guardarJSONArchivo(d, "vehiculos.json")
        """