#Recibir una cadena y darle la vuelta sin usar metodos especiales, solo utilizar estructuras de control

def invertido(texto):
    invertido = ""

    for letra in texto:
        invertido = letra + invertido
        
    if invertido == texto:
        print("Son palindromos")
    else:
        print("No son palindromos")


invertido("otto")