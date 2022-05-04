class Cama:
    __idCama=0
    __habitacion=0
    __estado=None
    __nomyap="" #Nombre y Apellido del paciente
    __diagnostico=""
    __fechainter=""
    __fechaalta=""

    def __init__(self, idc, habi, esta, nyaa, diag, fein, feal):
        self.__idCama= idc
        self.__habitacion= habi
        self.__estado= esta
        self.__nomyap= nyaa
        self.__diagnostico= diag
        self.__fechainter= fein
        self.__fechaalta= feal

    def getidCama(self):
        return self.__idCama
    def getHabitacion(self):
        return self.__habitacion
    def getEstado(self):
        return self.__estado
    def getNomyApe(self):
        return self.__nomyap
    def getDiagnostico(self):
        return self.__diagnostico
    def getFechaInter(self):
        return self.__fechainter
    def getFechaAlta(self):
        return self.__fechaalta

    def setEstado(self):
        self.__estado=False
    def setNyA(self):
        self.__nomyap=""
    def setFechaAlta(self, fecha):
        self.__fechaalta= fecha
