pares = []

for i in range(5):
    numero = int(input(f"Ingresa el número {i+1}: "))
    if numero % 2 == 0:
        pares.append(numero)
    
print("Números pares que ingresaste: ", pares)