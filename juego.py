from random import randint

import random

numAl = random.randint(1, 10)
print(numAl)

def main ():
        numero = input("Ingresa un numero del 1 al 10: ")
        while not numero.isdigit():
            numero = input("No has ingresado un número, intentálo de nuevo.")
        comparar(int(numero), numAl)

def comparar(n1, n2):
    if n1 > n2:
        print("El número ingresado es mayor que el que buscas")
        main()
    elif n1 < n2:
        print("El número ingresado es menor que el que buscas")
        main()
    else:
        print("Has acertado el número")

main()
