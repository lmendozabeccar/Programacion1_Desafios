productos = [
    [101, "AdidAS", 42, 3],
    [102, "NiKe", 40, 0],
    [103, "PumA", 35, 5],
    [104, "FIla", 39, 10],
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
print(Caracteres_recortados)

#Estandarizar el nombre de las marcas
for h in range(len(productos)):
    productos[h][1] = productos[h][1].lower()
print(productos)

#Ordenar de forma ascendente por stock y por marca de forma secundaria
