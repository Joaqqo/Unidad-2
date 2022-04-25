from Registro import Registro
import csv

class ManejadorRegistro:
    __listaRegistro= []

    def __init__(self): #Inciso 1
        self.__listaRegistro= [[] for x in range(30)] #Para crear una lista dentro de una lista, haciendola bidimensional

    def agregadorReg(self,regist,dia): #Inciso 2
        self.__listaRegistro[dia-1].append(regist)

    def MenorReg(self): #Inciso 3.1
        menorT, diaT, horaT=5000, 0, 0
        menorH, diaH, horaH=5000, 0, 0
        menorP, diaP, horaP=5000, 0, 0
        for i in range(len(self.__listaRegistro)):
            for j in range(len(self.__listaRegistro[i])):
                if self.__listaRegistro[i][j].getTemperatura() < menorT:
                    menorT= self.__listaRegistro[i][j].getTemperatura()
                    diaT=i+1
                    horaT=j
                if self.__listaRegistro[i][j].getHumedad() < menorH:
                    menorH= self.__listaRegistro[i][j].getHumedad()
                    diaH=i+1
                    horaH=j
                if self.__listaRegistro[i][j].getPresion() < menorP:
                    menorP= self.__listaRegistro[i][j].getPresion()
                    diaP=i+1
                    horaP=j
        return diaT, horaT, diaH, horaH, diaP, horaP #Retorna todos los valores que pide

    def MayorReg(self): #Inciso 3.1
        mayorT, diaT, horaT=0, 0, 0
        mayorH, diaH, horaH=0, 0, 0
        mayorP, diaP, horaP=0, 0, 0
        for i in range(len(self.__listaRegistro)):
            for j in range(len(self.__listaRegistro[i])):
                if self.__listaRegistro[i][j].getTemperatura() > mayorT:
                    mayorT= self.__listaRegistro[i][j].getTemperatura()
                    diaT=i+1
                    horaT=j
                if self.__listaRegistro[i][j].getHumedad() > mayorH:
                    mayorH= self.__listaRegistro[i][j].getHumedad()
                    diaH=i+1
                    horaH=j
                if self.__listaRegistro[i][j].getPresion() > mayorP:
                    mayorP= self.__listaRegistro[i][j].getPresion()
                    diaP=i+1
                    horaP=j
        return diaT, horaT, diaH, horaH, diaP, horaP #Retorna todos los valores que pide

    def Promedio(self,hora): #Inciso 3.2
        acumT=0 #Acumulador para hacer la cuenta del promedio
        for i in range(len(self.__listaRegistro)):
            acumT+= self.__listaRegistro[i][hora].getTemperatura()
        return (acumT/len(self.__listaRegistro)) #Retorna el Acumulador dividido en el "largo" de la lista para hacer el promedio

    def MostrarxDia(self,dia): #Inciso 3.3
        #Recibe un día y muestra los datos por ese día
        for i in range(len(self.__listaRegistro[dia-1])):
            print("{}-{}-{}-{}".format(i, self.__listaRegistro[dia-1][i].getTemperatura(),self.__listaRegistro[dia-1][i].getHumedad(),self.__listaRegistro[dia-1][i].getPresion()))



    def manejadorArchivo(self):
        archivo= open("mes.csv")
        reader= csv.reader(archivo, delimiter=';')
        for i in reader:
            dia= int(i[0])
            #salteamos la hora
            temp=int(i[2])
            hume=int(i[3])
            pres=float(i[4])
            objeto= Registro(temp, hume, pres)
            self.agregadorReg(objeto,dia)
        archivo.close()






