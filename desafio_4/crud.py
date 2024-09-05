from random import randint
encabezado_calificaciones = [
    ["Legajos", "Algebra", "Programación", "Análisis", "Sistemas", "Desarrollo web"]
]

aleatorio = lambda: randint(1, 10)

seguir = lambda: int(input("Quiere repetir el procedimiento?\n1 Si\n2 No\nElija un número: ")) == 1 
#Si el input es 1, la funcion devuelve True. Si es 2, devuelve False

mostrar_calificacion = lambda lista: [print(f"|{legajo:^8}|{algebra:^12}|{programacion:^12}|{analisis:^8}|{sistemas:^8}|{desarrollo:^14}|") for legajo, algebra, programacion, analisis, sistemas, desarrollo in lista] 
#Uso de corchetes solo para el print

def llenar_matriz(lista):
    for i in range(9):
        lista.append([1000+i, aleatorio(), aleatorio(), aleatorio(), aleatorio(), aleatorio()])
    return lista

def ingreso_notas():
    flag = True
    algebra =int(input("Ingrese la nueva nota de algebra: "))
    programacion =int(input("Ingrese la nueva nota de Programacion: "))
    analisis =int(input("Ingrese la nueva nota de analisis: "))
    sistemas =int(input("Ingrese la nueva nota de sistemas: "))
    desarrolloweb =int(input("Ingrese la nueva nota de desarrolloweb: "))
    return algebra, programacion, analisis, sistemas, desarrolloweb

def agregar_alumno(lista):
    flag_while = True
    while flag_while == True: #Esto es solo para verificar si el legajo existe
        calif = ingreso_notas() #Esta funcion me va a devolver una tupla
        lista.append([lista[-1][0]+1,calif[0],calif[1],calif[2],calif[3],calif[4]]) #Append de cada posicion de la tupla
        if seguir() == False:
            flag_while = False
    return lista

'''def mostrar_calificacion(lista):
    for legajo, algebra, programacion, analisis, sistemas, desarrollo in lista:
        print(f"|{legajo:^8}|{algebra:^12}|{programacion:^12}|{analisis:^8}|{sistemas:^8}|{desarrollo:^14}|")
    return 1'''

def actualizar_alumno(lista):
    flag = True
    while flag == True:
        posicion = []
        while posicion == []:
            legajo_actualizar = int(input("Ingrese el legajo que quiere actualizar: "))
            posicion = [i for i in range(len(lista)) if lista[i][0] == legajo_actualizar] #Saco en qué posicion esta el legajo en la lista
            if posicion == []:
                print("No se ha podido encontrar ese legajo, ingrese otro.")
        print("-"*26)
        print(lista[posicion[0]])#Lo imprimo para que el usuario vea lo que hay en la fila
        print("-"*26)
        calif = ingreso_notas()
        lista[posicion[0]] = [legajo_actualizar,calif[0],calif[1],calif[2],calif[3],calif[4]]
        print("Legajo actualizado")
        print("-"*26)
        if seguir() == False:
            flag = False
    return lista

def eliminar_alumno(lista):
    flag = True
    while flag == True:
        legajo_eliminar = int(input("Ingrese el legajo que quiere eliminar: "))
        flag_for = [True for fila in lista if legajo_eliminar in fila]
        if flag_for != []: #si el flag existe
            for i in range(0, len(lista)):
                if legajo_eliminar == lista[i][0]:
                    lista.pop(i)
                    print("Legajo correctamente eliminado")
                    print("-"*26)
            if seguir() == False:
                flag = False
    return lista