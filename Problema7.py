numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Menú de opciones
print("Seleccione una opción:")
print("1. Mostrar una suma de los dos números")
print("2. Mostrar una resta de los dos números (el primero menos el segundo)")
print("3. Mostrar una multiplicación de los dos números")

opcion = input("Ingrese el número de la opción seleccionada: ")

# Desarrollo de opciones
if opcion == '1':
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif opcion == '2':
    resultado = numero1 - numero2
    print(f"La resta de {numero1} menos {numero2} es: {resultado}")
elif opcion == '3':
    resultado = numero1 * numero2
    print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
else:
    print("La opción ingresada no es correcta.")