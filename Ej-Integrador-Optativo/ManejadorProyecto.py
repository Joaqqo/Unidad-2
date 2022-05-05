from Proyecto import Proyecto
import csv

class ManejadorProyecto:
    __listaProyectos=[]

    def __init__(self):
        self.__listaProyectos=[]

    def agregadorProyectos(self, proyecto):
        self.__listaProyectos.append(proyecto)




    def calculoGrupos(self, manI): # Calcula los puntos de los grupos
        for i in range(len(self.__listaProyectos)):
            idPr=self.__listaProyectos[i].getIdProyectoo()
            resultado= manI.calculoA(idPr)
            if resultado >= 3:
                self.__listaProyectos[i].AcumulaPuntos(10)
            else:
                self.__listaProyectos[i].AcumulaPuntos(-20)
                print("El proyecto con id {} debe tener como mínimo 3 integrantes".format(idPr))
#-------------------------------------------------------------------------------------------------- Separador
            director, categoriaD= manI.calculoByD(idPr)
            if director == False:
                print("El proyecto {} debe tener un Director" .format(idPr))
            if categoriaD == True:
                self.__listaProyectos[i].AcumulaPuntos(10)
            elif categoriaD == False:
                self.__listaProyectos[i].AcumulaPuntos(-5)
                print("El Director del Proyecto {} debe tener categoría I o II" .format(idPr))
#-------------------------------------------------------------------------------------------------- Separador
            codirector, categoriaC= manI.calculoCyE(idPr)
            if codirector == False:
                print("El proyecto {} debe tener un Codirector" .format(idPr))
            if categoriaC == True:
                self.__listaProyectos[i].AcumulaPuntos(10)
            elif categoriaC == False:
                self.__listaProyectos[i].AcumulaPuntos(-5)
                print("El Codirector del Proyecto {} debe tener categoría I, II o III" .format(idPr))


    def Ordena(self):
        for i in range(len(self.__listaProyectos)):
            for j in range(len(self.__listaProyectos)):
                if self.__listaProyectos[j]>self.__listaProyectos[i]:
                    aux=self.__listaProyectos[i]
                    self.__listaProyectos[i]=self.__listaProyectos[j]
                    self.__listaProyectos[j]=aux

    def mostrarOrdenado(self):
        self.Ordena()
        for i in range(len(self.__listaProyectos)):
            print("En {}° posición con {} puntos queda: {} ({})" .format(i+1, self.__listaProyectos[i].getPuntos(), self.__listaProyectos[i].getTitulo(), self.__listaProyectos[i].getIdProyectoo()))

    def manejadorArchivo(self):
        archi=open("proyectos.csv")
        reader= csv.reader(archi,delimiter=';')
        next(reader)
        for i in reader:
            idPr=str(i[0])
            titu=str(i[1])
            palC=str(i[2])
            objeto=Proyecto(idPr,titu,palC)
            self.agregadorProyectos(objeto)
        archi.close()



