edad = int(input("Ingresa tu edad: "))

if 0 < edad <=12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif 18 <= edad <= 59:
    print("Eres un adulto.")
else:
    print("Eres un anciano.")