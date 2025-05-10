#Christian Aarón Martínez Ibarra, 240247
#Ejercicio 4. Lista de pares. Función que reciba una lista de enteros y devuelva una nueva con los pares.

def lista_pares(lista):
    pares = []  #lista vacía
    for numero in lista:  #recorre cada elemento de la lista original
        if numero % 2 == 0:  #verificar si es par
            pares.append(numero)  #si es paro, se añade a la lista de pares
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
resultado = lista_pares(numeros)
print(f"Números pares: {resultado}")
