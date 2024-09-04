from random import randint
encabezado_calificaciones = [
    ["Legajos", "Algebra", "Programación", "Análisis", "Sistemas", "Desarrollo web"]
]

def aleatorio():
    return randint(1, 10)

def llenar_matriz(lista):
    for i in range(31): #######Simplificar
        lista.append([1000+i, aleatorio(), aleatorio(), aleatorio(), aleatorio(), aleatorio()])
    return lista

def seguir():
    respuesta = int(input("Quiere repetir el procedimiento?\n1 Si\n2 No\nElija un número: "))
    if respuesta == 2:
        return False
    else:
        return True

def ingreso_notas():
    algebra =int(input("Ingrese la nueva nota de algebra: "))
    programacion =int(input("Ingrese la nueva nota de Programacion: "))
    analisis =int(input("Ingrese la nueva nota de analisis: "))
    sistemas =int(input("Ingrese la nueva nota de sistemas: "))
    desarrolloweb =int(input("Ingrese la nueva nota de desarrolloweb: "))
    return algebra, programacion, analisis, sistemas, desarrolloweb

def agregar_alumno(lista):
    flag_while = True
    while flag_while == True: #Esto es solo para verificar si el legajo existe
        calif = ingreso_notas()
        lista.append([lista[-1][0]+1,calif[0],calif[1],calif[2],calif[3],calif[4]])
        if seguir() == False:
            flag_while = False
    return lista

def actualizar_alumno(lista):
    flag = True
    while flag == True:
        posicion = []
        while posicion == []:
            legajo_actualizar = int(input("Ingrese el legajo que quiere actualizar: "))
            posicion = [i for i in range(len(lista)) if lista[i][0] == legajo_actualizar]
            print(posicion)
            if posicion == []:
                print("No se ha podido encontrar ese legajo, ingrese otro.")
        print("-"*26)
        print(lista[posicion[0]])
        print("-"*26)
        calif = ingreso_notas()
        lista[posicion[0]] = [legajo_actualizar,calif[0],calif[1],calif[2],calif[3],calif[4]]
        print("Legajo actualizado")
        print("-"*26)
        if seguir() == False:
            flag = False
    return lista

def main():
    matriz = llenar_matriz(encabezado_calificaciones)
    respuesta = int(input("1 Agregar alumno\n2 Mostrar calificaciones\n3 Modificar alumno\n4 Eliminar alumno\n5 Finalizar\nIngrese el numero para la operación que desee: "))
    if respuesta == 1:
        agregar_alumno(matriz)
    elif respuesta == 2:
        "b"
    elif respuesta == 3:
        actualizar_alumno(matriz)
    elif respuesta == 4:
        "d"
    else:
        print("Fin del proceso")
main()