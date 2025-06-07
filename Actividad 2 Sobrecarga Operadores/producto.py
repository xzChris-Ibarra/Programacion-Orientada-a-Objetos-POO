
class Producto:
    def __init__(self, nombre, precio=0.0, cantidad=0):
       #Validaciones de tipos
       if not isinstance(nombre, str):
           raise TypeError("Error. El nombre debe ser una cadena de texto.")
       if not isinstance(precio, (int, float)):
           raise TypeError("Error. El precio debe ser un número.")
       if not isinstance(cantidad, int):
           raise TypeError("Error.La cantidad debe ser un número entero.")
       #Validar valores
       if precio < 0:
           raise ValueError("Error. El precio no puede ser negativo.")
       if cantidad < 0:
           raise ValueError("Error. La cantidad no puede ser negativa.")
       
       self.nombre = nombre
       self.precio = float(precio)
       self.cantidad = cantidad

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:,.2f} | Cantidad: {self.cantidad}"
    
    def __add__(self, otro):
        if isinstance(otro, Producto) and self.nombre == otro.nombre:
            cantidad_nueva = self.cantidad + otro.cantidad
            return Producto(self.nombre, self.precio, cantidad_nueva)
        else:
            raise ValueError("Error. Solo se pueden sumar productos con el mismo nombre.")
    
    def __mul__(self, cantidad):
        if isinstance(cantidad, int):
            return self.precio * cantidad
        else:
            raise TypeError("Error. Solo se puede multipliciar por un número entero.")
    
    def __eq__(self, otro):
        return isinstance(otro, Producto) and self.nombre == otro.nombre and self.precio == otro.precio
    
    def __del__(self):
        print(f"Eliminando producto: {self.nombre}")
    