#EJ 7
from random import randint
def main():
    valor = randint(1, 500)
    print(valor)
    intentos = 0
    while intentos < 5:
        try:
            n = int(input("Adivine el numero que está entre 1 y 500: "))
        except ValueError:
            print("Debe ingresar un numero.")
        else:
            if n == valor:
                print("Adivinaste")
                break
            elif n > valor:
                print("El valor es menor al que ingresaste")
            else:
                print("El valor es mayor al que ingresaste")
            intentos += 1
    return "-------------------------\nTe has quedado sin intentos"
print(main())