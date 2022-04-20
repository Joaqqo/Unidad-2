from ViajeroFrecuente import ViajeroFrecuente
import csv

class ManejadorViajeroFrecuente:
    __listaViajero= []

    def __init__(self):
        self.__listaViajero= []

    def agregadorViajero(self, viajero):
        self.__listaViajero.append(viajero)

    def manejadorArchivo(self):
        archivo= open("viajeros.csv")
        reader= csv.reader(archivo, delimiter=';')
        for i in reader:
            numviaj= int(i[0])
            dni= int(i[1])
            nomb= str(i[2])
            apel= str(i[3])
            mill= int(i[4])
            objeto= ViajeroFrecuente(numviaj, dni, nomb, apel, mill)
            self.agregadorViajero(objeto)
        archivo.close()

    def Verificacionn(self, num):
        bandera= False
        i=0
        while bandera==False and i<len(self.__listaViajero):
            if num == self.__listaViajero[i].getNumViajero():
                bandera= True
            i+=1
        return 1


    def getViajeros(self, num):
        return self.__listaViajero[num-1]

