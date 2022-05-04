class Medicamento:
    __idCama=0
    __idMedicamento=0
    __nombComer=""
    __monodroga=""
    __presentacion=""
    __cantAplicada=0
    __precio=0.0

    def __init__(self, idc, idm, noc, mon, pre, caa, prt):
        self.__idCama= idc
        self.__idMedicamento= idm
        self.__nombComer= noc
        self.__monodroga= mon
        self.__presentacion= pre
        self.__cantAplicada= caa
        self.__precio= prt

    def getidCamam(self):
        return self.__idCama
    def getidMedica(self):
        return self.__idMedicamento
    def getNombreComercial(self):
        return self.__nombComer
    def getMonodroga(self):
        return self.__monodroga
    def getPresentacion(self):
        return self.__presentacion
    def getCantidadAplicada(self):
        return self.__cantAplicada
    def getPrecio(self):
        return self.__precio
