from Integrante import Integrante
import numpy as np
import csv

class ManejadorIntegrantes:
    __ArregloIntegrantes=None

    def __init__(self):
        self.__ArregloIntegrantes=None



    def agregadorIntegrantes(self,integrante):
        self.__ArregloIntegrantes.append(integrante)


    def calculoA(self, id):
        cont=0
        for i in range(len(self.__ArregloIntegrantes)):
            if self.__ArregloIntegrantes[i].getIdProyecto() == id:
                cont+=1
        return cont


    def calculoByD(self, id):
        director=False
        categoria=False
        for i in range(len(self.__ArregloIntegrantes)):
            if self.__ArregloIntegrantes[i].getRol() == "director" and director == False:
                director=True
            if self.__ArregloIntegrantes[i].getIdProyecto() == id and self.__ArregloIntegrantes[i].getRol() == "director" and categoria == False:
                if self.__ArregloIntegrantes[i].getCategoriaInvestigacion()== "I" or self.__ArregloIntegrantes[i].getCategoriaInvestigacion()== "II":
                    categoria=True
        return director, categoria


    def calculoCyE(self, id):
        codirector=False
        categoriaC=False
        for i in range(len(self.__ArregloIntegrantes)):
            if self.__ArregloIntegrantes[i].getRol() == "codirector" and codirector == False:
                codirector=True
            if self.__ArregloIntegrantes[i].getIdProyecto() == id and self.__ArregloIntegrantes[i].getRol() == "codirector" and categoriaC == False:
                if self.__ArregloIntegrantes[i].getCategoriaInvestigacion() == "I" or self.__ArregloIntegrantes[i].getCategoriaInvestigacion() == "II" or self.__ArregloIntegrantes[i].getCategoriaInvestigacion() == "III":
                    categoriaC=True
        return codirector, categoriaC

    def manejadorArchivo(self):
        j=0
        cantidad=11
        self.__ArregloIntegrantes= np.empty(cantidad, dtype=Integrante)
        archivo=open("integrantesProyecto.csv")
        reader= csv.reader(archivo,delimiter=';')
        next(reader)
        for i in reader:
            idP=str(i[0])
            ayn=str(i[1])
            dni=str(i[2])
            cat=str(i[3])
            rol=str(i[4])
            integrr=Integrante(idP,ayn,dni,cat,rol)
            self.__ArregloIntegrantes[j]=integrr
            j+=1
        archivo.close()


