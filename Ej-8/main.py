from Conjunto import Conjunto
import os
def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1- Union de conjuntos')
        print('\n 2- Resta de conjuntos')
        print('\n 3- Igualdad de conjuntos')
        print('\n 4- Salir')
        opcion = int(input('\n Ingrese un OPCION: '))
        if(opcion == 1):
            union= conj1+conj2
            print(union)
        if(opcion == 2):
            resta= conj1-conj2
            print(resta)
        if(opcion == 3):
            igual= conj1==conj2
            print("Los conjuntos {}son iguales" .format("" if igual==True else "no "))
        if(opcion == 4):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')





if __name__ == "__main__":
    conj1 = Conjunto()
    conj2 = Conjunto()
    print("----Ingreso de valores del primer conjunto----")
    conj1.manejadorConjunto()
    print("----Ingreso de valores del segundo conjunto----")
    conj2.manejadorConjunto()
    menu()
