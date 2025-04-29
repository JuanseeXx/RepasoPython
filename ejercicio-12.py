frutas = ['Manzana', 'Pera', 'Piña']

print("Lista de frutas: ", frutas)
fruta_eliminar = input("Ingrese el nombre de la fruta que desee eliminar: ")

if fruta_eliminar in frutas:
    frutas.remove(fruta_eliminar)
    print("Fruta eliminada correctamente.")
else:
    print("Esa fruta no está en la lista.")

print("Lista actualizada: ", frutas)