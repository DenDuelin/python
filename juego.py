from random import randint

import random
numAl = random.randint(1, 10)
print(numAl)

def main ():
    numero = int(input("Ingresa un numero del 1 al 10: "))
    comparar(numero, numAl)

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