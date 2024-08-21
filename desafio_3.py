productos = [
    [101, "AdidAS", 42, 3],
    [102, "NiKe", 40, 0],
    [103, "PumA", 35, 5],
    [104, "FIla", 39, 9],
    [105, "adidAs", 40, 1],
    [106, "PUma", 44, 2],
    [107, "converse", 41, 3],
]
#Zapatillas, dividido en: id | Marca | Talle | stock 
#sorted con iterables

#Recortar para aquellas marcas que tienen un maximo de 4 caracteres
Caracteres_recortados = list()
for id, marca, talle, stock in productos:
    Caracteres_recortados.append([id, marca[:4], talle, stock])
productos = Caracteres_recortados[:]

#Estandarizar el nombre de las marcas
for h in range(len(productos)):
    productos[h][1] = productos[h][1].lower()
print(productos)

#Ordenar de forma ascendente por stock y por marca de forma secundaria
productos = sorted(productos, key=lambda x: (x[3], x[1]))

#Mostrar la lista de forma clara
print(f"|{"id":^5}|{"marca":^7}|{"talle":^7}|{"stock":^7}|")
for id, marca, talle, stock in productos:
    print(f"|{id:^5}|{marca:^8}|{talle:^6}|{stock:^5}|")

