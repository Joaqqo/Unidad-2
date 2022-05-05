class Proyecto:
    __idProyecto= ""
    __titulo= ""
    __palabrasClave= ""
    __puntos= 0

    def __init__(self, id, titulo, palclave):
        self.__idProyecto=id
        self.__titulo=titulo
        self.__palabrasClave=palclave
        self.__puntos= 0

    def __str__(self):
        return ("{} {} {} {}" .format(self.__idProyecto, self.__titulo, self.__palabrasClave, self.__puntos))

    def getIdProyectoo(self):
        return self.__idProyecto
    def getTitulo(self):
        return self.__titulo
    def getPalabrasClave(self):
        return self.__palabrasClave
    def AcumulaPuntos(self, puntos):
        self.__puntos+=puntos
    def getPuntos(self):
        return self.__puntos
    def __gt__(self,OtrosPuntos):
        return self.__puntos<OtrosPuntos.__puntos
