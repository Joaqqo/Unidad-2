class Registro:
    __temperatura= 0
    __humedad= 0
    __presion= 0.0

    def __init__(self, tem, hum, pre):
        self.__temperatura= tem
        self.__humedad= hum
        self.__presion= pre



    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presion
