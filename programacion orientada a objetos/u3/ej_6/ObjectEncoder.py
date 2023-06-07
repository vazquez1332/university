import json
from pathlib import Path
from clase_nuevo import Vehiculonuevo
from clase_usado import VehiculoUsado

class ObjectEncoder(object):

    def decodificarDiccionario(self, d, manejador):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            if class_name=='ManejaAutos':
                lista=d['lista']
                dLista = lista[0]
            for i in range(len(lista)):
                dLista=lista[i]
                class_name=dLista.pop('__class__')
                class_=eval(class_name)
                atributos=dLista['__atributos__']
                vehiculo=class_(**atributos)
                manejador.agregarAuto(vehiculo)
    
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
        
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
    
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)