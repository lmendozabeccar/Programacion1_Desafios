matriz_datos = [["Lucas Fernandez", "Argentina", "Buenos Aires", "Lanus", "Brasil",  "4521", "4241-1234"],
                ["Juan Perini", "Argentina", "Buenos Aires", "Lomas de Zamora", "Quintino",  "32", "4241-1234"],
                ["Maria Gonzarian", "Armenia", "Erevan", "Erevan", "Treina y tres orientales",  "43", "4241-1234"],
                ["Pedro Rodriguez", "España", "Madrid", "Madrid", "Castro Barros",  "453", "4241-1234"],
                ["Jose Lopini", "Italia", "Roma", "Roma", "Estados Unidos",  "432", "4241-1234"],
                ["Ana Martirol", "Argentina", "Buenos Aires", "Lanus", "Justo",  "765", "4241-1234"],
                ["Carlos Sancorz", "Argentina", "Buenos Aires", "Lomas de Zamora", "Muñiz",  "098", "4241-1234"],
                ["Laura Polnian", "Armenia", "Erevan", "Erevan", "Cabildo",  "543", "4241-1234"],
                ["Florencia Torrez", "España", "Madrid", "Madrid", "Libertador",  "99", "4241-1234"],
                ["Martin Gomini", "Italia", "Roma", "Roma", "Coronel Diaz",  "1234", "654-1234"],
                ["Lorenzo Suquini", "Argentina", "Buenos Aires", "Lanus", "Escobar",  "110", "4241-1234"],
                ["Sol Arraian", "Argentina", "Buenos Aires", "Lomas de Zamora", "Laje",  "336", "4241-1234"]]

with open("C:\\Users\\Lucas\\Desktop\\Lucas\\Facultad\\Progra1\\Trabajo-archivos\\DATOS.TXT", mode="w", encoding="UTF-8") as datos:
    for fila in matriz_datos:
        for dato in fila:
            datos.write(dato + ";")
        datos.write("\n")