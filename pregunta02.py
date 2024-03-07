monto_consumo = float(input("Ingrese el monto de consumo: $"))
porcent_propina = float(input("Ingrese el porcentaje de propina: %"))

cant_propina = monto_consumo*(porcent_propina/100) 

print("La cantidad de propina a dejar es:", cant_propina)
