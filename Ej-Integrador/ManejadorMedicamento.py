from Medicamento import Medicamento
import csv

class ManejadorMedicamento:
    __listaMedicamento=[]

    def __init__(self):
        self.__listaMedicamento= []

    def agregadorMedicamento(self, meds):
        self.__listaMedicamento.append(meds)

    def MostrarDatos(self, idcama):
        adeudado=0 #Adeudado es el precio total que debe pagar el cliente en medicamentos
        for i in range(len(self.__listaMedicamento)):
            if self.__listaMedicamento[i].getidCamam() == idcama:
                adeudado+= self.__listaMedicamento[i].getPrecio()
                print("{:<14} {:<16} {:^21} {:>6} {:>14}" .format(self.__listaMedicamento[i].getNombreComercial(), self.__listaMedicamento[i].getMonodroga(), self.__listaMedicamento[i].getPresentacion(), self.__listaMedicamento[i].getCantidadAplicada(), self.__listaMedicamento[i].getPrecio()))
        return adeudado





    def manejadorArchivo(self):
        archivo= open("medicamentos.csv")
        reader= csv.reader(archivo, delimiter=";")
        next(reader)
        for i in reader:
            medc=Medicamento(int(i[0]), int(i[1]), i[2], i[3], i[4], int(i[5]), float(i[6]))
            self.agregadorMedicamento(medc)
        archivo.close()

