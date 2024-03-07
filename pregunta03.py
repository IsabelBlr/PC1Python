peso_payaso = 112
peso_muñeca = 75

num_payaso = int(input("Ingrese el numero de payasos vendidos en el ultimo pedido: "))
num_muñeca = int(input("Ingrese el numero de muñeca vendidos en el ultimo pedido: "))

peso_total = (peso_payaso*num_payaso) + (peso_muñeca*num_muñeca)

print("El peso total del paquete a enviar es: ", peso_total,"gramos.")