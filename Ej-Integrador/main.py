from ManejadorCama import ManejadorCama
from ManejadorMedicamento import ManejadorMedicamento
import os


def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Alta de paciente')
        print('\n 2-Pacientes por diagnóstico')
        print('\n 3- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            nombyap=input("Ingrese el nombre del paciente que quiera dar de alta:  ")
            idcama=manC.BuscaNombre(nombyap)
            if idcama == -1:
                print("Nombre erróneo, ingrese de nuevo.")
            else:
                fechh= input("Ingrese la Fecha de Alta(dd/mm/aaaa):  ")
                manC.MostrarDatos(idcama, fechh)
                print("Medicamento/monodroga                Presentación      Cantidad      Precio")
                preciototal= manM.MostrarDatos(idcama)
                print("Total adeudado: {:>60}" .format(preciototal))

        if(opcion == 2):
            diagnst=input("Ingrese el diagnóstico del cual desea ver los pacientes:  ")
            manC.MostrarxDiag(diagnst)
        if(opcion == 3):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')


if __name__ == '__main__':
    cams=int(input("Ingrese la cantidad de camas: "))
    manC= ManejadorCama(cams)
    manM= ManejadorMedicamento()
    manC.manejadorArchivo()
    manM.manejadorArchivo()
    menu()
