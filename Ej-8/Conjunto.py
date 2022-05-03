class Conjunto:
    __listaConjunto=[]

    def __init__(self):
        self.__listaConjunto=[]
    def __str__(self):
        return ("{}".format(self.__listaConjunto))

    def agregadorConjunto(self,num):
        self.__listaConjunto.append(num)
    def getLista(self):
        return self.__listaConjunto
    def manejadorConjunto(self):
        num=int(input("Ingrese el número que desea agregar al conjunto(finalice con 0): "))
        while num!=0:
            self.agregadorConjunto(num)
            num=int(input("Ingrese el número que desea agregar al conjunto(finalice con 0): "))

    def __add__(self, otroConjunto):
        lista1= self.__listaConjunto
        lista1.extend(otroConjunto.getLista()) #Para agregar la segunda lista a la lista1
        a=len(lista1)
        i=0
        while i < a:
            if lista1.count(lista1[i])>=2: #El count cuenta cuantas veces se repite un elemento
                lista1.remove(lista1[i]) #Remove para remover ese elemento repetido
                a=a-1
            i+=1
        lista1.sort() #Ordena la lista de menor a mayor
        return lista1

    def __sub__(self, otroConjunto):
        lista1= self.__listaConjunto
        lista2= otroConjunto.getLista()
        a=len(lista1)
        i=0
        while i < a:
            if lista2.count(lista1[i]) != 0: #Si existe algún repetido en la lista2 de la lista1
                lista1.remove(lista1[i]) #Removemos ese repetido de la lista 1
                a=a-1
            i+=1
        lista1.sort() #Ordenamos la lista de menor a mayor
        return lista1
    def __eq__(self, otroConjunto):
        lista1= self.__listaConjunto
        lista2= otroConjunto.getLista()
        a=len(lista1)
        i=0
        equal=True #Equal para retornar
        while i < a:
            if lista1.count(lista1[i]) != lista2.count(lista1[i]): #En el caso que el .count() sea distinto en alguna instancia, es que los conjuntos serán distintos
                i=a
                equal= False #Equal toma valor False
            i+=1
        return equal


