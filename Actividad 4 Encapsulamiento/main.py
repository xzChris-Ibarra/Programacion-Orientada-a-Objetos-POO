#Menú interactivo

from cuenta import Cuenta, CuentaPremium

def menu():
    cuentas = []

    while True:
        print("\n--- Menú de Cuentas Bancarias ---")
        print("1. Crear cuenta")
        print("2. Ver saldo")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Ver beneficios (Premium)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del titular: ")
            tipo = input("Tipo de cuenta (ahorro/corriente): ").lower()
            saldo = float(input("Saldo inicial: "))
            premium = input("¿Cuenta premium? (s/n): ").lower()

            if premium == "s":
                beneficios = input("Beneficios: ")
                cuenta = CuentaPremium(nombre, saldo, tipo, beneficios)
            else:
                cuenta = Cuenta(nombre, saldo, tipo)

            cuentas.append(cuenta)
            print("Cuenta creada exitosamente.")

        elif opcion == "2":
            for i, c in enumerate(cuentas):
                print(f"[{i}] ", end="")
                c.mostrar_saldo()

        elif opcion == "3":
            idx = int(input("Ingresa el número de cuenta: "))
            monto = float(input("Cantidad a depositar: "))
            cuentas[idx].depositar(monto)

        elif opcion == "4":
            idx = int(input("Ingresa el número de cuenta: "))
            monto = float(input("Cantidad a retirar: "))
            cuentas[idx].retirar(monto)

        elif opcion == "5":
            for c in cuentas:
                if isinstance(c, CuentaPremium):
                    c.mostrar_beneficios()

        elif opcion == "6":
            print("Saliendo del programa. ¡Gracias!")
            break

        else:
            print("Opción no válida.")

menu()
