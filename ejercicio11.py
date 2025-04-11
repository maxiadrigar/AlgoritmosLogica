## Crea una funcion que nos diga cual es la raiz cuadrada mas grande de 3 numeros

def raiz_mayor(n1,n2,n3):

    rnum1 = n1**(1/2)
    rnum2 = n2**(1/2)
    rnum3 = n3**(1/2)

    rmax = rnum1
    if rnum2 > rnum1:
        rmax = rnum2
    if rnum3 > rnum2:
        rmax = rnum3

    return rmax

print(raiz_mayor(64,81,100))
