## Crea una funcion que cuente cuantas vocales hay en cada palabra de una lista

lista_palabras = ['entrevista','tecnica','perro','python','murcielago']

def contar_vocales(palabras: list) -> list:
    vocales = "aeiouAEIOU"

    return [sum(1 for letra in palabra  if letra in vocales)  for palabra in palabras]

print(contar_vocales(lista_palabras))