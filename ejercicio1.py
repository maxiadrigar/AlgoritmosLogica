## Dado un numero, devuelva su tabla de multiplicar

def multiplicar(n):

    print(f"Tabla del {n}")

    for i in range(1,11):
        print(f"{n} * {i} = {n * i}")

while True:
    print("Ingrese un numero para ver su tabla de multiplicar")
    print("Presione X para finalizar")
    entrada = input("Ingrese aqui: ")
    print("")

    if entrada.lower() == "x":
        print(f"[!] Saliendo...")
        break
    
    if entrada.isdigit():
        n = int(entrada)
        multiplicar(n)
    else:
        print("Ingrese una opcion valida o 'X' para salir")    