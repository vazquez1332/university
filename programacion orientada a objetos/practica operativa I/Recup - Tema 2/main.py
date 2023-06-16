from manejadorAfiliados import ManejadorAfiliado
from manejadorAtenciones import ManejadorAtenciones
from menu import Menu

if __name__=="__main__":
    manejador_afiliados=ManejadorAfiliado("afiliados.csv")
    manejador_atenciones=ManejadorAtenciones("atenciones.csv", manejador_afiliados)

    menu=Menu(manejador_atenciones, manejador_afiliados)