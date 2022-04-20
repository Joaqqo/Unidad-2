class Registro:
    __temperatura= 0
    __humedad= 0
    __presion= 0

    def __init__(self, tem, hum, pre):
        self.__temperatura= tem
        self.__humedad= hum
        self.__presion= pre

    def __str__(self):
        print("|{}|{}|{} " .format(self.__temperatura, self.__humedad, self.__presion))

    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presion
