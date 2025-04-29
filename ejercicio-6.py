hora = int(input("Ingresa la hora actual (0-23): "))

if hora < 12 or hora > 18:
    print("No es hora de trabajar.")
else:
    print("Es hora de trabajar.")