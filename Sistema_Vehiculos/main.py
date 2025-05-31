from vehiculo import Vehiculos

vehiculo1 = Vehiculos("Infiniti", "FX35", 2004)
vehiculo2 = Vehiculos("Ford", "Raptor", 2020)

print("Información inicial de los vehiculos")
vehiculo1.mostrar_info()
vehiculo2.mostrar_info()

vehiculo1.cumplir_año()
vehiculo2.cumplir_año()

print("Información actual de los autos: ")
vehiculo1.mostrar_info()
vehiculo2.mostrar_info()
