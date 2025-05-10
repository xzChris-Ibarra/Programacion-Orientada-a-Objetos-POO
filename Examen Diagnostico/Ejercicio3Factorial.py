#Christian Aarón Martínez Ibarra, 240247
#Ejercicio 3. Función recursiva que calcula el factorial de un número n.

def factorial(a):
    if a == 0 or a == 1:
        return 1  #base para evitar ciclo infinito de un caso
    else:
        return a * factorial(a - 1)  #call recursiva

a = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {a} es: {factorial(a)}")
