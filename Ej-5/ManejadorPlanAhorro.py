from PlanAhorro import PlanAhorro
import csv

class ManejadorPlanAhorro:
    __listaPlanAhorro=[]

    def __init__(self):
        self.__listaPlanAhorro=[]

    def agregadorPlan(self, plan):
        self.__listaPlanAhorro.append(plan)

    def modifValor(self): #Inciso 2a
        for i in range(len(self.__listaPlanAhorro)):
            print("CÓDIGO: {} - MODELO: {} - VERSIÓN: {}".format(self.__listaPlanAhorro[i].getCodigoPlan(), self.__listaPlanAhorro[i].getModelo(), self.__listaPlanAhorro[i].getVersion()))
            vactual=float(input("Ingrese el nuevo valor del vehículo:  "))
            self.__listaPlanAhorro[i].cambiarValor(vactual)

    def mostrarPorCuota(self, cuota): #Inciso 2b
        for i in range(len(self.__listaPlanAhorro)):
            if self.__listaPlanAhorro[i].getValorCuota() < cuota:
                print("COD: {} - MODELO{} - VERSIÓN: {}" .format(self.__listaPlanAhorro[i].getCodigoPlan(), self.__listaPlanAhorro[i].getModelo(), self.__listaPlanAhorro[i].getVersion()))

    def mostrarValorCuota(self): #Inciso 2c
        for i in range(len(self.__listaPlanAhorro)):
            print("COD: {} - CUOTA: {} - LICITAR: {}".format(self.__listaPlanAhorro[i].getCodigoPlan(), self.__listaPlanAhorro[i].getValorCuota(), self.__listaPlanAhorro[i].getValorCuota()*self.__listaPlanAhorro[i].getCuotasLicita()))
        

    def manejadorArchivo(self):
        archivo= open("planes.csv")
        reader= csv.reader(archivo, delimiter=";")
        for i in reader:
            cod=int(i[0])
            mod=str(i[1])
            ver=str(i[2])
            val=float(i[3])
            objeto= PlanAhorro(cod,mod,ver,val)
            self.agregadorPlan(objeto)
        archivo.close()
