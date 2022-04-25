from ManejadorRegistro import ManejadorRegistro
import os

def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Dia y hora de menor y mayor valor')
        print('\n 2-Promedio de temperatura por hora')
        print('\n 3-Mostrar registros por día')
        print('\n 4- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            print("---------------------------------------------------------------------------------")
            menor=manReg.MenorReg()
            print("Día y hora con menor Temperatura: {} - {} " .format(menor[0], menor[1]))
            print("Día y hora con menor Humedad: {} - {}" .format(menor[2], menor[3]))
            print("Día y hora con menor Presión: {} - {}" .format(menor[4], menor[5]))
            print("---------------------------------------------------------------------------------")
            mayor=manReg.MayorReg()
            print("Día y hora con mayor Temperatura: {} - {}" .format(mayor[0], mayor[1]))
            print("Día y hora con mayor Humedad: {} - {}" .format(mayor[2], mayor[3]))
            print("Día y hora con mayor Presión: {} - {}" .format(mayor[4], mayor[5]))
            print("---------------------------------------------------------------------------------")
        if(opcion == 2):
            print("---------------------------------------------------------------------------------")
            print("HORA - PROMEDIO")
            for i in range(24):
                prom=manReg.Promedio(i)
                print("{} - {}" .format(i, prom))
            print("---------------------------------------------------------------------------------")

        if(opcion == 3):
            print("---------------------------------------------------------------------------------")
            day=int(input("Ingrese el día que desea ver: "))
            print("HORA-TEMP-HUME-PRES")
            manReg.MostrarxDia(day)
            print("---------------------------------------------------------------------------------")

        if(opcion == 4):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')

if __name__ == '__main__':
    manReg= ManejadorRegistro()
    manReg.manejadorArchivo()
    menu()
