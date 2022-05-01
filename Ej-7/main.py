from ViajeroFrecuente import ViajeroFrecuente


if __name__ == '__main__':
    VF=ViajeroFrecuente(1,"40308485","Franco","Andino",100)
    print("-------------------------------------------------")
    print(VF)
    print("-------------------------------------------------")
    mill=int(input("Ingrese las millas a comparar:  "))
    print("El viajero {}tiene las mismas millas acumuladas que las ingresadas" .format(""if VF==mill else "no ")) #Por izquierda
    print("-------------------------------------------------")
    mill=int(input("Ingrese las millas a comparar:  "))
    print("El viajero {}tiene las mismas millas acumuladas que las ingresadas" .format(""if mill==VF else "no ")) #Por derecha
    print("-------------------------------------------------")
    mill=int(input("Ingrese las millas que desea acumular:  "))
    VF= mill + VF
    print(VF)
    print("-------------------------------------------------")
    mill=int(input("Ingrese las millas que desea restar:  "))
    VF= mill - VF
    print(VF)
    print("-------------------------------------------------")
