from Cama import Cama
import numpy as np
import csv

class ManejadorCama:
    __cantidad=0
    __dimension=0
    __incremento=5

    def __init__(self, dimension, incremento=5):
        self.__ArregloCama= np.empty(dimension, dtype=Cama)
        self.__cantidad= 0
        self.__dimension= dimension

    def agregadorCama(self, camm):
        if self.__cantidad == self.__dimension:
            self.__dimension+= self.__incremento
            self.__ArregloCama.resize(self.__dimension)
        self.__ArregloCama[self.__cantidad]= camm
        self.__cantidad+= 1

    def BuscaNombre(self,nombre):
        i=0
        while i < self.__cantidad:
            if self.__ArregloCama[i].getNomyApe().lower() == nombre.lower(): #.lower() para comparar las cadenas sin mayúsculas
                break
            else:
                i+=1
        if i < self.__cantidad:
            return self.__ArregloCama[i].getidCama()
        else:
            return -1

    def MostrarDatos(self, idcama, fecha):
        self.__ArregloCama[idcama-1].setFechaAlta(fecha) #Para setear la fecha que le dan el alta
        self.__ArregloCama[idcama-1].setEstado() #Para que la cama quede como desocupada
        print("Paciente: {:<12}       Cama: {:>1}   Habitación: {:>3}" .format(self.__ArregloCama[idcama-1].getNomyApe(), self.__ArregloCama[idcama-1].getidCama(), self.__ArregloCama[idcama-1].getHabitacion()))
        print("Diagnóstico: {:<5}   Fecha de internación: {:<12}" .format(self.__ArregloCama[idcama-1].getDiagnostico(), self.__ArregloCama[idcama-1].getFechaInter()))
        print("Fecha Alta: {:<2}" .format(self.__ArregloCama[idcama-1].getFechaAlta() ))
        self.__ArregloCama[idcama-1].setNyA() #Para que se muestre que no hay nadie ocupando la cama

    def MostrarxDiag(self, diagnst):
        for i in range(len(self.__ArregloCama)):
            if self.__ArregloCama[i].getDiagnostico().lower() == diagnst.lower():
                if self.__ArregloCama[i].getEstado(): #Comprueba si la cama está ocupada o no
                    print("Cama: {} - Habitación: {} - Apellido y Nombre: {} - Fecha de internación: {}" .format(self.__ArregloCama[i].getidCama(), self.__ArregloCama[i].getHabitacion(), self.__ArregloCama[i].getNomyApe(), self.__ArregloCama[i].getFechaInter()))

    def manejadorArchivo(self):
        archivo= open("camas.csv")
        reader= csv.reader(archivo, delimiter=";", skipinitialspace = True)
        next(reader)
        for i in reader:
            camaa=Cama(int(i[0]), int(i[1]), i[2], i[3], i[4], i[5], i[6])
            self.agregadorCama(camaa)
        archivo.close()
