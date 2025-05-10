#Christian Aarón Martínez Ibarra, 240247
#Ejercicio 5. Validación de contraseña.

password = "admin123"
intentos = 0  #contador intentos

while intentos < 3:
    acceso = input("Ingrese la contraseña: ")
    if acceso == password:
        print("Acceso correcto. Bienvenido.")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta.")
if intentos == 3:
    print("Acceso bloqueado, intentos agotados.")
