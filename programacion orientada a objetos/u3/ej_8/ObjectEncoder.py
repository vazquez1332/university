import json
from pathlib import Path
from clase_personal import Personal
from clase_docente import Docente
from clase_investigador import Investigador
from clase_personalApoyo import PersonalApoyo
from clase_docente_investigador import DocenteInvestigador

class ObjectEncoder(object):
    def decodificarDiccionario(self, d, manejador):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            if class_name=='ManejaPersonal':
                lista=d['lista']
                dLista = lista[0]
            for i in range(len(lista)):
                dLista=lista[i]
                class_name=dLista.pop('__class__')
                class_=eval(class_name)
                atributos=dLista['__atributos__']
                personal=class_(**atributos)
                manejador.agregarElemento(personal)
    
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