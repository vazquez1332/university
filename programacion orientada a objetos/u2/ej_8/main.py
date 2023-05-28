from claseConjunto import Conjunto
from claseMenu import Menu

def test():
    conjunto1=Conjunto({1,2,3,4})
    conjunto2=Conjunto({4,5,6,7})
    Menu(1,conjunto1,conjunto2)
    Menu(2,conjunto1,conjunto2)
    Menu(3,conjunto1,conjunto2)

if __name__=="__main__":
    test()