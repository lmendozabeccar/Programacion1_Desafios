matriz_datos = []

with open(r"C:\Users\Lucas\Desktop\Lucas\Facultad\Progra1\Trabajo-archivos\DATOS.TXT", mode="r", encoding="UTF-8") as datos:
    flag = True
    while flag:
        line = datos.readline().strip()
        if line == "":
            flag = False
        else:
            line = line.split(";")
            line.remove("")
            matriz_datos.append(line)
print(matriz_datos)