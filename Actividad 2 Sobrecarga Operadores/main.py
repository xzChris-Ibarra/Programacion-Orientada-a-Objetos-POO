from producto import Producto

p1 = Producto("Laptop", 8000, 5)
p2 = Producto("Laptop", 8000, 8)
p3 = Producto("Teclado", 850, 3)

print(p1)
print(p1 + p2)
print(p3 * 3)
print(p1 == p2)

del p1
del p2
del p3
