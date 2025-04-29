numeros = [15, 29, 19, 23, 24, 45]

print(numeros)
numero = int(input("Ingrese el número a insertar: "))
posicion = int(input("En que posición deseas insertar el número? (0 a 5): "))

numeros.insert(posicion, numero)

print("Lista actualizada: ", numeros)