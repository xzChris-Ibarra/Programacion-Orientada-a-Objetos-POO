#Christian Aarón Martínez Ibarra, 240247
#Ejercicio 1: Número mayor. Recibir 3 números como parámetros y devolver el mayor.

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if b < a > c:
    numero_mayor = a
    print(f"El número mayor es: {numero_mayor}")
elif a < b > c:
    numero_mayor = b
    print(f"El número mayor es: {numero_mayor}")
else:
    numero_mayor = c
    print(f"El número mayor es: {numero_mayor}")
