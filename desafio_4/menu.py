from crud import llenar_matriz, agregar_alumno, mostrar_calificacion, actualizar_alumno, eliminar_alumno, encabezado_calificaciones
def menu():
    flag = True
    matriz = llenar_matriz(encabezado_calificaciones)
    while flag == True:
        respuesta = int(input("1 Agregar alumno\n2 Mostrar calificaciones\n3 Modificar alumno\n4 Eliminar alumno\n5 Finalizar\nIngrese el numero para la operación que desee: "))
        if respuesta == 1:
            matriz = agregar_alumno(matriz)
        elif respuesta == 2:
            mostrar_calificacion(matriz)
        elif respuesta == 3:
            matriz = actualizar_alumno(matriz)
        elif respuesta == 4:
            matriz = eliminar_alumno(matriz)
        else:
            print("Fin del proceso")
            flag = False
menu()