class Vehiculos:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print("---" * 20)

    def cumplir_año(self):
        self.año += 1
        print(f"El vehiculo {self.marca} {self.modelo} ha cumplido otro año más")

