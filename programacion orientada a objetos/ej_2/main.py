from viajero import Viajero

def test():
     #datos correctos
     viajero_correcto=Viajero(7,"0110","Liliana","Lopez",700)
     print(f"Cantidad total de millas: {viajero_correcto.cantidadTotaldeMillas()}")
     print(f"Acumular millas: {viajero_correcto.acumularMillas(1000)}")
     print(f"Canjear millas: {viajero_correcto.canjearMillas(500)}")

     #datos incorrectos 
     try:
          viajero_incorrecto=Viajero("tres", "abcdefgh", "Nombre", "Apellido", "mil")
     except ValueError:
         pass
     try:
        print(f"Cantidad total de millas: {viajero_incorrecto.cantidadTotaldeMillas()}")
     except Exception as e:
        print(f"Error: {e}")
        pass
     try:
        print(f"Acumular millas: {viajero_incorrecto.acumularMillas(1000)}")
     except Exception as e:
        print(f"Error: {e}")
        pass
     try:
        print(f"Canjear millas: {viajero_incorrecto.canjearMillas(500)}")
     except Exception as e:
        print(f"Error: {e}")
        pass

if __name__=="__main__":
    test()
    lista=Viajero.opening()
    print("\n")
    seleccionado=Viajero.obtenerViajero(int(input("Ingrese el numero de viajero: \n")), lista)
    Viajero.Menu()
    opcion=int(input("Ingrese la opcion: \n"))
    while opcion != 0:
        if opcion == 1:
             print(f"La cantidad de millas es: {seleccionado.cantidadTotaldeMillas()}\n")
        elif opcion == 2:
             millas = int(input("Ingrese la cantidad de millas a acumular: \n"))
             print(f"La nueva cantidad de millas es: {seleccionado.acumularMillas(millas)}\n")
        elif opcion == 3:
             millas = int(input("Ingrese la cantidad de millas a canjear: \n"))
             if seleccionado.canjearMillas(millas):
               print("La cantidad de millas acumuladas es: %d"%(seleccionado.getMillasAcum()))
        else:
             print("Opcion incorrecta\n")  
        opcion = int(input("Ingrese la opcion: \n"))


 