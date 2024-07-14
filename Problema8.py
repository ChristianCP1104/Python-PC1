time = input("Ingrese la hora en formato de 24 horas (hh:mm): ")

# Separar la hora y los minutos
horas, minutos = time.split(":")
horas = int(horas)
minutos = int(minutos)

time_float = horas + minutos / 60.0

# Determinar si es la hora de alguna comida
if 7 <= time_float < 9:  
    print("Es la hora del desayuno.")
elif 12 <= time_float < 14:  
    print("Es la hora del almuerzo.")
elif 18 <= time_float < 20: 
    print("Es la hora de la cena.")
