
def contar_palabras(frase, busqueda):

    frase = frase.lower()
    conteo = frase.count(busqueda)
    print(f"La palabra {busqueda} aparace {conteo} veces")

contar_palabras("soy una palabra en una frase, PALABRA ", "palabra")


#frase = "hola soy una frase"
#palabra = "frase"

#conteo = frase.count(palabra)
#print(conteo)
