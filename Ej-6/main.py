from ManejadorViajeroFrecuente import ManejadorViajeroFrecuente


if __name__ == '__main__':
    manVA=ManejadorViajeroFrecuente()
    manVA.manejadorArchivo()
    print("-------------------------------------------------")
    numv=manVA.maxiMillas()
    print("Viajero con mayor cantidad de millas es: ")
    print(numv)
    print("-------------------------------------------------")
    numv=int(input("Ingrese el número del viajero que desea acumular millas:  "))
    VF= manVA.getViajeros(numv)
    mill=int(input("Ingrese las millas que desea acumular:  "))
    VF+= mill
    print(VF)
    print("-------------------------------------------------")
    numv=int(input("Ingrese el número del viajero que desea restar millas:  "))
    VF= manVA.getViajeros(numv)
    mill=int(input("Ingrese las millas que desea restar:  "))
    VF-= mill
    print(VF)
    print("-------------------------------------------------")
