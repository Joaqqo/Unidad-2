class Integrante:
    __idProyecto= ""
    __apellidoNombre= ""
    __dni= ""
    __categoriaInvestigacion: ""
    __rol: ""

    def __init__(self, id, ayn, dni, cat, rol):
        self.__idProyecto=id
        self.__apellidoNombre=ayn
        self.__dni=dni
        self.__categoriaInvestigacion=cat
        self.__rol=rol

    def __str__(self):
        return ("{} {} {} {} {}" .format(self.__idProyecto, self.__apellidoNombre, self.__dni, self.__categoriaInvestigacion, self.__rol))

    def getIdProyecto(self):
        return self.__idProyecto
    def getApellidoNombre(self):
        return self.__apellidoNombre
    def getDNI(self):
        return self.__dni
    def getCategoriaInvestigacion(self):
        return self.__categoriaInvestigacion
    def getRol(self):
        return self.__rol
