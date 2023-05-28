from viajeroFrecuente import ViajeroFrecuente
def test():
     viajero1=ViajeroFrecuente("1","1234","Santiago","Vazquez","1000")
     viajero2=ViajeroFrecuente("2","4321","Ana","Castro","500")

     assert viajero1>viajero2
     try: 
         assert viajero2>viajero1,"Error, las millas acumuladas del segundo viajero no son mas que las del primero. "
     except AssertionError as error: 
          print(f"{error}")
          pass
     
     viajero3=viajero1+500
     assert viajero3.get_millas_acum()==1500, "Error al sumar millas"
     viajero4=viajero2-100
     assert viajero4.get_millas_acum()==400, "Error al restar millas al viajero"

if __name__=="__main__":
    test()
