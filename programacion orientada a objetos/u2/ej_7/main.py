from viajeroFrecuente import ViajeroFrecuente

def test():
     v1=ViajeroFrecuente("1", "12345678", "Santiaguito", "Vazquez", "150")
     print(v1==100)  # False
     print(200==v1)  # False
     print(150==v1)  # True
     print("\n")

     v2=100+v1
     print(v2==250)  # True
     print(v2==110)  # False
     print("\n")

     v3=100-v1
     print(v3==50)   # True
     print(v3==(-50)) #False

if __name__=="__main__":
    test()


 