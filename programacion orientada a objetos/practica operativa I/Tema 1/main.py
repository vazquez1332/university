from gestorInfracciones import GestorInfracciones
from gestorInfractores import GestorInfractores
from menu import Menu
from os import path

if __name__ == '__main__':
	gestorInfractores = GestorInfractores(path.dirname(__file__) + '/infractores.csv')
	gestorInfracciones = GestorInfracciones(path.dirname(__file__) + '/infracciones.csv', gestorInfractores)
	menu = Menu(gestorInfracciones, gestorInfractores)
	menu.iniciar()
