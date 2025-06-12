#Clase base que representa a un empleado general
class Empleado:
    def __init__(self, nombre, salario):
        #Validar tipos
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(salario, (int, float)) or salario < 0:
            raise ValueError("El salario debe ser un número mayor o igual a 0.")
        
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Salario: ${self.salario:,.2f}")

#Clase hija que representa a un Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        #Constructor de la clase padre
        super().__init__(nombre, salario)
        if not isinstance(departamento, str):
            raise TypeError("El departamento debe ser una cadena de texto.")
        
        self.departamento = departamento

    def mostrar_info(self):
        #Sobrescribir método y usar super
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")

# Clase hija que representa a un Técnico
class Tecnico(Empleado):
    def __init__(self, nombre, salario, especialidad):
        super().__init__(nombre, salario)
        if not isinstance(especialidad, str):
            raise TypeError("La especialidad debe ser una cadena de texto.")
        
        self.especialidad = especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}")

#Clase hija que representa a un tecnico
class Tecnico(Empleado):
    def __init__(self, nombre, salario, especialidad):
        super().__init__(nombre, salario)
        if not isinstance(especialidad, str):
            raise TypeError("La especialidad debe ser una cadena de texto.")
        
        self.especialidad = especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}")

