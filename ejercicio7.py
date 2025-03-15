# Enunciado: Dibujar un cuadrado hueco con asterisctos, indicando en la funcion los lados del cuadrado

# Ejemplo}
# Cuadrado(4)
# Devuelve

# ****
# *  *
# *  *
# ****

def cuadrado(lados):
    for x in range(0, lados):
        for i in range (0, lados):
            if x == 0 or x == lados-1 or i == 0 or i == lados-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print(cuadrado(4))


