class PlanAhorro:
    CuotasPlan=60
    CuotLicit=10
    __codPlan=0
    __modelo=""
    __version=""
    __valorAuto=0.0


    def __init__(self, cod, mod, ver, val):
        self.__codPlan= cod
        self.__modelo= mod
        self.__version= ver
        self.__valorAuto= val

    @classmethod
    def getCuotasPlan(cls):
        return cls.CuotasPlan
    @classmethod
    def getCuotasLicita(cls):
        return cls.CuotLicit

    def getCodigoPlan(self):
        return self.__codPlan
    def getModelo(self):
        return self.__modelo
    def getVersion(self):
        return self.__version
    def getValorAuto(self):
        return self.__valorAuto

#valorcuota= ((importe vehiculo/cant cuotas) + importe vehiculo *0.10), lo cambié al de abajo para que dé un resultado lógico
#valorcuota=((importe vehículo+(importe vehículo*0.10))/cant cuotas

    def cambiarValor(self, valornuevo): #Para cambiar el valor de un vehículo
        self.__valorAuto= valornuevo
    def getValorCuota(self): #Para obtener el valor de una cuota
        porce=self.__valorAuto*0.10
        cuota=(self.__valorAuto+porce)/PlanAhorro.CuotasPlan
        return cuota


