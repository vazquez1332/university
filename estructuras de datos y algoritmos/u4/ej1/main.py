from arbol_bb import Arbol

if __name__ == "__main__":

    arbol = Arbol()

    try:
        datos = [20, 10, 30, 5, 15, 25, 35]
        for dado in datos:
            arbol.insertar(dado)

        arbol.mostrar(arbol.getRaiz())

    except Exception as e:
        print(str(e))
 