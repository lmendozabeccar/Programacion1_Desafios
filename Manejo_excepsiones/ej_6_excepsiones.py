#EJ 6
lista = []
while True:
    try:
        n = int(input("Ingrese un número: "))
        if n == -1:
            break
    except:
        print("tiene que ingresar un número")
        break
    lista.append(n)
try: 
    busq = int(input("Ingrese que valor desea buscar en la lista: "))
    index_ = lista.index(busq)
except ValueError:
    print("No se encontró el numero en la lista")
else:
    print(f"Se encontró el número en la posicion {index_} de la lista")