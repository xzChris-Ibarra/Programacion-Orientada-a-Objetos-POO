class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  #privado

    def saludar(self):
        print(f"Hola, mi nombre es {self.__nombre}")

class Ejemplo:
    def __init__(self):
        self.publico = "acceso libre"
        self._protegido = "acceso limitado"
        self.__privado = "acceso restringido"

class Cuenta:
    def __init__(self):
        self.__saldo = 1000

c = Cuenta()
#print(c.__saldo)  #Error
print(c._Cuenta__saldo)  #Funciona (pero no recomendado)

class Producto:
    def __init__(self, precio):
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido")
