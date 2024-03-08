lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

posiciones_a_eliminar = [0, 4, 5]
for posicion in sorted(posiciones_a_eliminar, reverse=True):
    lista.pop(posicion)

print(lista)