from empleado import Empleado, Gerente, Tecnico

#Crear objetos de las clases
empleado1 = Empleado("Carlos", 12000)
gerente1 = Gerente("María", 25000, "Ventas")
tecnico1 = Tecnico("Luis", 15000, "Redes")

#Mostrar inf
print("\nInformación de Empleado:")
empleado1.mostrar_info()

print("\nInformación de Gerente:")
gerente1.mostrar_info()

print("\nInformación de Técnico:")
tecnico1.mostrar_info()

#Comprobar el tipo de cada objeto con isinstance
print("\nVerificaciones con isinstance:")
print(isinstance(gerente1, Empleado)) 
print(isinstance(tecnico1, Tecnico))  
print(isinstance(empleado1, Gerente))  
