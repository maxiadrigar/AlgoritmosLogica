#Crea una función llamada promedio_calif que te diga el promedio de una cantidad arbitraria de calificaciones

def promedio_calif(*calif):

    resultado = sum(calif)/len(calif)
    return resultado

print(promedio_calif(69,73,88,45,90,77,88,71,62,59))