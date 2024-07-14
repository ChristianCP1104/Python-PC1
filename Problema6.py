edad = int(input("Ingrese la edad del cliente: "))

# Determinar el precio de la entrada basado en la edad
if edad < 4:
    precio = 0
    print("La entrada es gratis.")
elif 4 <= edad <= 18:
    precio = 5
    print(f"El precio de la entrada es: ${precio}")
else:
    precio = 10
    print(f"El precio de la entrada es: ${precio}")
