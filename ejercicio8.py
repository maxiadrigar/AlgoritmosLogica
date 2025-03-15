#Enunciado: Dado dos numeros, contar cuantos numeros impares hay entre ellos
## Ejemplo:
## impares(1, 100) // Devuelve 49

def cantidad_impares(num1, num2):

    contador = 0
    for i in range(num1, num2):
        if i % 2 == 1:
            print(f"El numero {i} es impar")
            contador += 1
    return f"Numeros impares: {contador}"

print(cantidad_impares(1, 100))
    