#EJ10
def eliminarclaves(dic, claves):
    cont = 0
    for i in claves:
        if i in dic:
            dic.pop(i)
            cont+=1
    return dic, cont

dic = {
    'Pais': "Argentina",
    'Provincia': "Cordoba",
    'Localidad': "Villa General Belgrano",
    'Calle': "Senillosa",
    'Numero': 835    
}
claves = ['Pais', 'Localidad']
print(eliminarclaves(dic, claves))