monto_consumo = float(input("Ingrese el monto de su consumo en el restaurante: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar por la atencion: "))

propina = monto_consumo * (porcentaje_propina / 100)

print(f"La cantidad de propina a dejar es: ${propina:.2f}")
