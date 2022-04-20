from Registro import Registro
import csv

class ManejadorRegistro:
    __listaReg=[]
    __listaRegistro= []

    def __init__(self): #31 filas y 24 columnas (31 días y 24 horas)
        self.__listaReg=[]
        self.__listaRegistro= [[0 for y in range(24)] for x in range(31)]
#        for i in range (31): #20
#            self.__listaRegistro.append([])
#            for j in range(24): #45
#                self.__listaRegistro[i].append(0)

    def agregadorRegistro(self,dia,hora,reg):
        self.__listaRegistro[dia-1][hora]= reg

    def agregadorReg(self, registro,dia,hora):
        self.__listaReg.append(registro)
        self.__listaRegistro[dia-1][hora]=self.__listaReg[-1]
        #self.agregadorRegistro(dia,hora,self.__listaReg[-1]) #como hacer para llevar el último elemento de la lista
        #(osea el que se acaba de agregar)



    def manejadorArchivo(self):
        archivo= open("mes.csv")
        reader= csv.reader(archivo, delimiter=';')
        for i in reader:
            dia= int(i[0])
            hora=int(i[1])
            temp=int(i[2])
            hume=int(i[3])
            pres=int(i[4])
            objeto= Registro(temp, hume, pres)
            self.agregadorReg(objeto,dia,hora)
        archivo.close()

    def Mostrar(self):
        print(self.__listaRegistro[0][0])


