
## Enunciado 6: Cuando es el X% de X numero?
# Ejemplos:
# tantoPorCiento(20, 100) // Devuelve 20 

def porcentajeNum(porcentaje, numero):

    resultado = (numero * porcentaje) / 100
    return f"El {porcentaje} % de {numero} = {resultado}"

print(porcentajeNum(12, 190)) 