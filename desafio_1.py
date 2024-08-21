import random
matriz = []
materias = ["Algebra", "Analisis", "Ingles", "Calculo"]
estudiantes = ["Juan", "Pepe", "Ivan", "Raul", "Gian", "Luca"]
def aleatorio():
    return random.randint(1, 10)

def mostrar_matriz(matriz, estudiantes, materias):
    print("   Nombre   ", end=" |      ")
    for n in range(len(materias)):
        if n != 3:
            print(materias[n], end="      |      ")
        elif n == 3:
            print(materias[n], "      |")
    for i in range(len(matriz)):
        for x in range(len(matriz[0])):
            if x == 0:
                print("   ", estudiantes[i], end="     |")
            if x < 3:
                print("        ", matriz[i][x], end="         |")
            elif x == 3:
                print("        ", matriz[i][x], "       |")

def calcular_promedio_estudiantes(matriz):
    for i in range(0, len(matriz)):
        sumador = 0
        for x in range(0, len(matriz[0])):
            sumador += matriz[i][x]
            #print(i, ":", matriz[i][x])
        promedio = sumador / len(matriz[0])
        if i == 0:
            promedio_est_0 = promedio
        elif i == 1:
            promedio_est_1 = promedio
        elif i == 2:
            promedio_est_2 = promedio
        elif i == 3:
            promedio_est_3 = promedio
        elif i == 4:
            promedio_est_4 = promedio
        else:
            promedio_est_5 = promedio
    return promedio_est_0, promedio_est_1, promedio_est_2, promedio_est_3, promedio_est_4, promedio_est_5
def calcular_promedio_materias(matriz):
    promedio_alg = 0
    promedio_ana = 0
    promedio_ing = 0
    promedio_cal = 0
    for i in range(0, len(matriz)):
        for x in range(0, len(matriz[0])):
            if x == 0:
                promedio_alg += matriz[i][x]
            elif x == 1:
                promedio_ana += matriz[i][x]
            elif x == 2:
                promedio_ing += matriz[i][x]
            else:
                promedio_cal += matriz[i][x]
    return promedio_alg/6, promedio_ana/6, promedio_ing/6, promedio_cal/6
for i in range(len(estudiantes)):
    matriz.append([]) 
    for x in range(len(materias)):
        matriz[i].append(aleatorio())

print(mostrar_matriz(matriz, estudiantes, materias))

tupla_promedios_materias = calcular_promedio_materias(matriz)
tupla_promedios_estudiantes = calcular_promedio_estudiantes(matriz)

for i in range(len(estudiantes)):
       print("Promedio de", estudiantes[i], ":", tupla_promedios_estudiantes[i])
print("---------------------------------------------")

for u in range(0, len(materias)):
       print("Promedio de", materias[u], ":", tupla_promedios_materias[u])