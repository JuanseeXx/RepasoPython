tarea = input("¿Terminaste tu tarea? (s/n): ")

if tarea == 'n':
    print("Debes terminar la tarea.")
elif tarea == 's':
    print("Perfecto. Puedes salir a jugar")
else:
    print("Opción inválida. Ingrese 's' para sí y 'n' para no.")