#Crea una función que reciba una cantidad arbitraria de argumentos y calcule el producto de multiplicarlos todos entre ellos

def multiplicar(*args):
    producto = 1

    for numero in args:
        producto = numero * producto
    return producto

print(multiplicar(2,3,6,10))