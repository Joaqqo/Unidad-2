

class Ventana:
    __titulo=""
    __coordXizq=0 #Coordenada X vértice superior izquierda
    __coordYizq=0 #Coordenada Y vértice superior izquierda
    __coordXder=0 #Coordenada X vértice inferior derecho
    __coordYder=0 #Coordenada Y vértice inferior derecho

    def __init__(self, tit, xizq=0, yizq=0, xder=500, yder=500):
        self.__titulo= tit
        self.__coordXizq= xizq
        self.__coordYizq= yizq
        self.__coordXder= xder
        self.__coordYder= yder

    def verificacion(self):
        if self.__coordXizq<0:
            return False
        if self.__coordYizq<0:
            return False
        if self.__coordXder>500:
            return False
        if self.__coordYder>500:
            return False
        if self.__coordXizq>self.__coordXder:
            return False
        if self.__coordYizq>self.__coordYder:
            return False

    def mostrar(self):
        verif= self.verificacion()
        if verif == False:
            print("Hubo un error con la validación de datos")
        else:
            print("({}),({}) - ({}),({})" .format(self.__coordXizq, self.__coordYizq, self.__coordXder, self.__coordYder))

    def getTitulo(self):
        return self.__titulo

    def ancho(self):
        result= self.__coordXder-self.__coordXizq
        return result

    def alto(self):
        result= self.__coordYder-self.__coordYizq
        return result

    def moverDerecha(self,var=0):
        self.__coordXizq+= var
        self.__coordXder+= var
    def moverIzquierda(self,var=0):
        self.__coordXizq-= var
        self.__coordXder-= var
    def bajar(self,var=0):
        self.__coordYizq-= var
        self.__coordYder-= var
    def subir(self,var=0):
        self.__coordYizq+= var
        self.__coordYder+= var
