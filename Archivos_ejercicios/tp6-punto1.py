nombres_apellidos_matriz = ["Lucas Fernandez\n", "Juan Perini\n", "Maria Gonzarian\n", "Pedro Rodriguez\n", "Jose Lopini\n", "Ana Martirol\n", "Carlos Sancorz\n", "Laura Polnian\n", "Florencia Torrez\n", "Martin Gomini\n", "Lorenzo Suquini\n", "Sol Arraian\n"]

with open(r"C:\Users\Lucas\Desktop\Lucas\Facultad\Progra1\Trabajo-archivos\NOMBRES.TXT", mode="w") as nombres_apellidos:
    nombres_apellidos.writelines(nombres_apellidos_matriz)
    
with open(r"C:\Users\Lucas\Desktop\Lucas\Facultad\Progra1\Trabajo-archivos\NOMBRES.TXT", mode="r") as nombres_apellidos:
    flag = True
    while flag:
        linea = nombres_apellidos.readline().strip()
        if linea == "":
            flag = False
        else:
            if linea[-3:] == "ian":
                armenia = open(r"C:\Users\Lucas\Desktop\Lucas\Facultad\Progra1\Trabajo-archivos\ARMENIA.TXT", mode="a")
                armenia.write(linea + "\n")
                armenia.close()
            elif linea[-3:] == "ini":
                italia = open(r"C:\Users\Lucas\Desktop\Lucas\Facultad\Progra1\Trabajo-archivos\ITALIA.TXT", mode="a")
                italia.write(linea + "\n")
                italia.close()
            elif linea[-2:] == "ez":
                españa = open(r"C:\Users\Lucas\Desktop\Lucas\Facultad\Progra1\Trabajo-archivos\ESPAÑA.TXT", mode="a")
                españa.write(linea + "\n")
                españa.close()