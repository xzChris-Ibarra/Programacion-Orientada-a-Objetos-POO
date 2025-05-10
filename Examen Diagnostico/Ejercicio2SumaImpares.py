#Christian Aarón Martínez Ibarra, 240247
"""
Ejercicio 2: Suma de Impares. Solicita al usuario un número entero positivo 'n' y calcula la 
suma de los números impares del 1 al 'n' usando un bucle for.
"""

a = int(input("Ingrese un número entero positivo: "))
suma_impar = 0

for i in range(1, a + 1): #recorre todos los números del 1 hasta a.
    if i % 2 != 0:        #verifica si el número es impar.
        suma_impar += i   #acumula los impares en la variable.

print(f"La suma de los impares del 1 al {a} es: {suma_impar}")
