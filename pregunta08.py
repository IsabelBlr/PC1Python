time = input("Ingrese la hora en formato HH:MM (24 horas): ")

hours, minutes = time.split(":")
hour_in_float = float(hours) + float(minutes) / 60  # Convertir a formato de horas con decimales

if 7 <= hour_in_float < 8:
    print("Es hora de desayunar.")
elif 12 <= hour_in_float < 13:
    print("Es hora de almorzar.")
elif 18 <= hour_in_float < 19:
    print("Es hora de cenar.")