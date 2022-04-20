from ManejadorViajeroFrecuente import ManejadorViajeroFrecuente
import os

def menu(num):
    indice= objeto.getViajeros(num)
    salir= False
    opcion= 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n Usted esta viendo los datos de: \n')
        print(indice.__str__())
        print('\n 1- Consultar cantidad de millas.')
        print('\n 2- Acumular Millas.')
        print('\n 3- Canjear Millas.')
        print('\n 4- Salir.')
        opcion = int(input('\n Ingrese un OPCION: '))
        if(opcion == 1):
            print("El viajero seleccionado acumula {} millas".format(indice.cantidadTotaldeMillas()))
        if(opcion == 2):
            millas= int(input("Ingrese la cantidad de millas recorridas del viajero:  "))
            indice.acumularMillas(millas)
        if(opcion == 3):
            canjear= int(input("Ingrese la cantidad de millas a canjear:  "))
            indice.canjearMillas(canjear)
        if(opcion == 4):
            salir = True
        os.system('cls')

if __name__ == '__main__':
    objeto=ManejadorViajeroFrecuente()
    objeto.manejadorArchivo()
    print(objeto) #almacenamiento en memoria
    numero=int(input("Ingrese el número del viajero:  "))
    verif= objeto.Verificacionn(numero)
    if(verif == 1):
        menu(numero)
    else:
        print("No existe ese número de viajero.")
