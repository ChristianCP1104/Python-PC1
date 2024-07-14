peso_payaso = 112  # peso en gramos
peso_muneca = 75   # peso en gramos

# Venta
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_munecas = int(input("Ingrese el número de muñecas vendidas: "))

# Calcular el peso total
peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

# Peso total del paquete
print(f"El peso total del paquete es: {peso_total} gramos")