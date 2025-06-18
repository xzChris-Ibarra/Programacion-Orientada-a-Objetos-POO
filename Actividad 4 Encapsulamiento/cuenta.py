class Cuenta:
    def __init__(self, titular, saldo, tipo):
        self.__titular = titular
        self.__saldo = saldo if saldo >= 0 else 0
        if tipo in ["ahorro", "corriente"]:
            self.__tipo = tipo
        else:
            raise ValueError("Tipo de cuenta inválido: debe ser 'ahorro' o 'corriente'")

    #Getters
    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_tipo(self):
        return self.__tipo

    #Setters
    def set_titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    def set_tipo(self, nuevo_tipo):
        if nuevo_tipo in ["ahorro", "corriente"]:
            self.__tipo = nuevo_tipo
        else:
            print("Tipo inválido")

    #Métodos principales
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo:.2f}")
        else:
            print("Cantidad inválida para depósito")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo:.2f}")
        else:
            print("Fondos insuficientes o cantidad inválida")

    def mostrar_saldo(self):
        print(f"Titular: {self.__titular} | Saldo: ${self.__saldo:.2f} | Tipo: {self.__tipo}")


#Subclase opcional
class CuentaPremium(Cuenta):
    def __init__(self, titular, saldo, tipo, beneficios):
        super().__init__(titular, saldo, tipo)
        self._beneficios = beneficios  #protegido

    def mostrar_beneficios(self):
        print(f"Beneficios exclusivos para {self.get_titular()}: {self._beneficios}")
