numeros = [15, 22, 35, 49, 72]

numero_buscado = int(input("Ingresa un número para buscar: "))

if numero_buscado in numeros:
    posicion = numeros.index(numero_buscado)
    print(f"El número {numero_buscado} está en la posición {posicion} de la lista.")
else:
    print(f"El número {numero_buscado} no está en la lista.")