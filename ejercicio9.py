## Arma una función que eleve al cuadrado todos los elementos de una lista. 
## Prueba con una lista con todos los numeros pares del 2 al 20.

lista = [i for i in range(1,21)]

def elevar_cuadrado(lista):
    cuadrados = []
    for i in lista:
        if i % 2 == 0:
            cuadrados += [i ** 2]
    return cuadrados

print(elevar_cuadrado(lista))



