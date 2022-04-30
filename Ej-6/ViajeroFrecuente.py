class ViajeroFrecuente:
    __numViajero= 0
    __dni= ""
    __nombre= ""
    __apellido= ""
    __millasAcum= 0

    def __init__(self, numviaj, dni, nom, ape, millasac):
        self.__numViajero= numviaj
        self.__dni= dni
        self.__nombre= nom
        self.__apellido= ape
        self.__millasAcum= millasac

    def __str__(self):
        return ("{}-{}-{}-{}-{}" .format(self.__numViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcum))


    def getNumViajero(self):
        return self.__numViajero
    def getMillasAcum(self):
        return self.__millasAcum

    def __add__(self, milla):
        return ViajeroFrecuente(self.__numViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcum+milla)
    def __sub__(self, milla):
        return ViajeroFrecuente(self.__numViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcum-milla)
    def __gt__(self,millas):
        return self.__millasAcum > millas.__millasAcum

