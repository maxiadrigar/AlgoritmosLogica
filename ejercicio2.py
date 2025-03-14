# Dado una cadena de texto, comprobar si es palindromo o no

def palindromo(texto):

    invertido = list(texto)
    invertido.reverse()
    invertido = ''.join(invertido)
    
    return (invertido == texto)

#print(palindromo("otto"))

def es_palindromo(texto):
    return texto == ''.join(reversed(texto))

def palindr(textual):
    return textual == textual[::-1]

print(f"Es palindromo la siguiente palabra? {palindr("oso")}")