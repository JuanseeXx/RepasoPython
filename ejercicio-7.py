licencia = input("¿Tienes licencia? (s/n): ")
casco = input("¿Llevas casco? (s/n): ")

if licencia == 'n' or casco == 'n':
    print("No puedes conducir.")
else:
    print("Puedes conducir, maneja con cuidado.")
