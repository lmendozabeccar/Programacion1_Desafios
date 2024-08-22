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

#CRUD
def crear_registro(productos):#Crear
    id = productos[-1][0] + 1
    marca = str(input("Ingrese la marca: "))
    talle = int(input("Ingrese el talle: "))
    stock = int(input("Ingrese el stock: "))
    productos.append([id, marca, talle, stock])
    return productos

def eliminar_registro(productos):
    id_eliminar = int(input("Ingrese el id del producto que desee eliminar: "))
    for i in range(len(productos)-1):
        if productos[i][0] == id_eliminar:
            productos.pop(i)
    return productos

def actualizar_registro(productos):
    id_act = int(input("Ingrese el id que desee actualizar: "))
    marca_act = 0
    talle_act = 0
    stock_act = 0
    for h in productos:
        if h[0] == id_act:
            marca_act == h[1]
            talle_act == h[2]
            stock_act == h[3]
    respuesta_m = int(input("Desea actualizar la marca?\n1.si\n2.no\nIngrese 1 o 2: "))
    if respuesta_m == 1:
        marca_act = str(input("Ingrese la marca: "))
    respuesta_t = int(input("Desea actualizar el talle?\n1.si\n2.no\nIngrese 1 o 2: "))
    if respuesta_t == 1:
        talle_act = int(input("Ingrese el talle nuevo: "))
    respuesta_s = int(input("Desea actualizar el stock?\n1.si\n2.no\nIngrese 1 o 2: "))
    if respuesta_s == 1:
        stock_act = int(input("Ingrese el stock: "))
    for i in productos:
        if i[0] == id_act:
            i == [id, marca_act, talle_act, stock_act]
    return productos

n = True   
while n == True:
    print("-" * 30)
    operacion = int(input("Operaciones:\n1.Agregar registro \n2.Eliminar registro \n3.Actualizar registro \n4.Finalizar\nSeleccione un numero (1, 2, 3 o 4): "))
    if operacion == 1:
        productos = crear_registro(productos)
    elif operacion == 2:
        productos = eliminar_registro(productos)
    elif operacion == 3:
        productos = actualizar_registro(productos)
    else:
        n=False
#Recortar para aquellas marcas que tienen un maximo de 4 caracteres

Caracteres_recortados = list()
for id, marca, talle, stock in productos:
    Caracteres_recortados.append([id, marca[:4], talle, stock])
productos = Caracteres_recortados[:]

#Estandarizar el nombre de las marcas
for h in range(len(productos)):
    productos[h][1] = productos[h][1].lower()

#Ordenar de forma ascendente por stock y por marca de forma secundaria
productos = sorted(productos, key=lambda x: (x[3], x[1]))

#Mostrar la lista de forma clara
print(f"|{"id":^5}|{"marca":^7}|{"talle":^7}|{"stock":^7}|")
for id, marca, talle, stock in productos:
    print(f"|{id:^5}|{marca:^8}|{talle:^6}|{stock:^5}|")