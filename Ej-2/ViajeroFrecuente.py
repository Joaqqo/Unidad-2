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
        return ("|NUM: {}|DNI: {}|NOM: {}|APE: {}|MIL: {}" .format(self.__numViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcum))

    def cantidadTotaldeMillas(self):
        return self.__millasAcum

    def acumularMillas(self, milla):
        self.__millasAcum+= milla

    def canjearMillas(self, milla):
        if self.__millasAcum >= milla:
            self.__millasAcum-= milla
            print("Sus millas fueron canjeadas.")
        else:
            print("No tiene las suficientes millas para canjear.")

    def getNumViajero(self):
        return self.__numViajero
