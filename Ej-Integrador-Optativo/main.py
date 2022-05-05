
from ManejadorIntegrantesProyecto import ManejadorIntegrantes
from ManejadorProyecto import ManejadorProyecto
if __name__ == "__main__":
    manejadorI= ManejadorIntegrantes()
    manejadorI.manejadorArchivo()
    manejadorP= ManejadorProyecto()
    manejadorP.manejadorArchivo()
    print("----------CALCULO DE PUNTOS----------")
    manejadorP.calculoGrupos(manejadorI)
    print("----------GRUPOS ORDENADOS-----------")
    manejadorP.mostrarOrdenado()
    print("-------------------------------------")
