#EJ6
def frase(palabra):
    conjunto = set(palabra.split())
    lista = list(conjunto)
    orden = sorted(lista, key=lambda lista: (len(lista), lista))
    return orden

print(frase('Tesla es el mejor auto de USA, siendo, a la vez, el auto más comprado de USA'))