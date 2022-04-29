from ManejadorPlanAhorro import ManejadorPlanAhorro
from PlanAhorro import PlanAhorro
import os


def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Actualizar valor de vehículo')
        print('\n 2-Valor de cuota inferior al ingresado')
        print('\n 3-Monto para licitar vehículo')
        print('\n 4-Modificar cantidad de cuotas para licitar')
        print('\n 5- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            manPA.modifValor()
        if(opcion == 2):
            valorc=float(input("Ingrese el valor de la cuota:  "))
            print("CODIGO - MODELO - ")
            manPA.mostrarPorCuota(valorc)
        if(opcion == 3):
            manPA.mostrarValorCuota()
        if(opcion == 4):
            lici=int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
            PlanAhorro.CuotLicit= lici #Inciso 2d

        if(opcion == 5):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')

if __name__ == '__main__':
    manPA= ManejadorPlanAhorro()
    manPA.manejadorArchivo()
    menu()
