class Conjunto:
    __elementos:set

    def __init__(self, elementos:set)->None:
        self.__elementos=elementos

    def __add__(self, otro:"Conjunto")->"Conjunto":
        return Conjunto(self.__elementos.union(otro.__elementos))

    def __sub__(self, otro:"Conjunto")->"Conjunto":
        return Conjunto(self.__elementos.difference(otro.__elementos))

    def __eq__(self, otro:"Conjunto")->bool:
        if len(self.__elementos)==len(otro.__elementos):
            return self.__elementos==otro.__elementos
        
    def __str__(self)->str:
        return f"{self.__elementos}"