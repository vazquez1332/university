from cola_secuencial import Cola
import random as rand

if __name__ == "__main__":
    tiempoFrecuencia = int(input("Ingrese la frecuencia de clientes: "))
    tiempoAtencion = int(input("Ingrese el tiempo de atencion: "))
    tiempoSimulacion = int(input("Ingrese el tiempo de simulacion: "))

    cola = Cola()
    
    cajero = 0
    cantAtendidos = 0
    tiempoTotal = 0
    
    for reloj in range(0, tiempoSimulacion, 1):
        valor = rand.random()

        if valor <= 1/tiempoFrecuencia:
            cola.insertar(reloj)

        if cajero == 0 and not cola.vacia():
            cajero = tiempoAtencion
            totalEspera = reloj - cola.suprimir()
            cantAtendidos += 1

        if cajero > 0:
            cajero -= 1
        
    tiempoTotal = totalEspera / cantAtendidos
    print(tiempoTotal)

