from clase_nodo import Nodo
from zope.interface import implementer
from interface import Imanejador
from clase_docente import Docente
from clase_investigador import Investigador
from clase_docente_investigador import DocenteInvestigador
from clase_personalApoyo import PersonalApoyo

@implementer (Imanejador)
class ManejaPersonal:
    __comienzo:Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
        
    def __iter__(self):
        return self
                     
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
        
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            lista=[dato.toJSON() for dato in self]
            )
        return d

    def CreaElemento(self):
        op = int(input("Ingrese opcion: 1-Docente 2-Investigador 3-Personal Apoyo 4-Docente Investigador: "))
        cuil = input("Ingrese cuil: ")
        apellido = input("Ingrese apellido: ") 
        nombre= input("Ingrese nombre: ")
        sueldo_basico = input("Ingrese sueldo básico: ")
        antiguedad = input("Ingrese antiguedad: ")
        if op == 1:
            carrera = input("Ingrese carrera: ")
            cargo = input("Ingrese cargo: ")
            catedra = input("Ingrese catedra: ")
            elemento = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, " ", " ")
        elif op == 2:
            area_investigacion = input("Ingrese area investigacion: ")
            tipo_investigacion = input("Ingrese tipo de investigacion: ")
            elemento = Investigador (cuil, apellido, nombre, sueldo_basico, antiguedad, " ", " ", " ", area_investigacion, tipo_investigacion)
        elif op == 3:
            categoria = input("Ingrese categoria: ")
            elemento = PersonalApoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, " ", " ", " ", " ", " ", categoria)
        elif op == 4:
            carrera = input("Ingrese carrera: ")
            cargo = input("Ingrese cargo: ")
            catedra = input("Ingrese catedra: ")
            area_investigacion = input("Ingrese area investigacion: ")
            tipo_investigacion = input("Ingrese tipo de investigacion: ")
            categoria_investigacion = input("Ingrese categoria investigacion: ")
            importe_extra = input("Ingrese importe extra: ")
            elemento = DocenteInvestigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion,categoria_investigacion,importe_extra)
        else:
            elemento = -1
            print("Ingreso opcion incorrecta")
        return elemento
    
    def insertarElemento(self, posicion, elemento):
        if posicion == 1:
            self.agregarElemento(elemento)
        else:
            nodo = Nodo(elemento)
            aux = self.__comienzo
            for i in range(0, posicion-1):
                prev = aux
                aux = aux.getSiguiente()
                
            prev.setSiguiente(nodo)
            nodo.setSiguiente(aux)
            
            self.__tope += 1
            
    def agregarElemento(self, elemento):
        nodo = Nodo(elemento)
        if self.__comienzo == None:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            nodo.setSiguiente(None)
            aux.setSiguiente(nodo)
            self.__tope += 1

    def MostrarElemento(self, posicion):
        for dato in self:
            if self.__indice == posicion:
                print(dato.__class__.__name__)
    
    def cuentaPorArea(self, area):
        contadorDI = 0
        contadorI = 0
        for dato in self:
            if area == dato.getArea_investigacion():
                if dato.__class__.__name__ =="DocenteInvestigador":
                    contadorDI += 1
                elif dato.__class__.__name__ == "Investigador":
                    contadorI += 1
        print("Investigadores: " + str(contadorI) + " Docentes investigadores: "+ str(contadorDI))
    
    def ordenaPorApellido(self):
        k = None
        cota = None
        while(k != self.__comienzo):
            k = self.__comienzo
            p = self.__comienzo
            while (p.getSiguiente()!= cota):
                if (p.getDato().getApellido() > p.getSiguiente().getDato().getApellido()):
                    aux = p.getSiguiente().getDato()
                    p.getSiguiente().setDato(p.getDato())
                    p.setDato(aux)
                    k = p
                p = p.getSiguiente()
            cota = k.getSiguiente()
    
    def Muestra(self):
        for dato in self:
            print(dato)      
            
    def listaPorCat(self, cat):
        suma = 0
        for dato in self:
            if dato.getCategoria() == cat:
                print(dato)
                suma += float(dato.getImporteExtra())
        
        print("Dinero a solicitar: " + str(suma))
        
    def listaOrdenadaNombre(self, carrera):
        lista = []
        for dato in self:
            if dato.getCarrera() == carrera and dato.__class__.__name__ == "DocenteInvestigador":
                lista.append(dato)
                
        lista.sort()
        for dato in lista:
            print(dato)