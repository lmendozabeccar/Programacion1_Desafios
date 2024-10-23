#EJ5
import math
def main():
    try:
        n = int(input("Ingrese un numero: "))
        return math.sqrt(n)
    except ValueError:
        return "Debe ingresar un número positivo"
    except:
        return "Ha ocurrido un error"
print(main())