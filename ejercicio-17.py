nombres = ["Juan", "Sebastian", "Pepe", "Juan", "Santiago", "Juan"]

nombre_buscado = input("Ingresa un nombre para buscar: ")

cantidad = nombres.count(nombre_buscado)
print(f"El nombre {nombre_buscado} aparece {cantidad} veces.")