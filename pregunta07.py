def mostrar_menu():
    print("¿Qué operación deseas realizar?")
    print("1. Mostrar la suma de los dos números")
    print("2. Mostrar la resta de los dos números (el primero menos el segundo)")
    print("3. Mostrar la multiplicación de los dos números")
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion

def suma(a, b):
    return a + b


def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

opcion = mostrar_menu()

if opcion == '1':
    print("La suma de los números es:", suma(num1, num2))
elif opcion == '2':
    print("La resta de los números es:", resta(num1, num2))
elif opcion == '3':
    print("La multiplicación de los números es:", multiplicacion(num1, num2))
else:
    print("Opción no válida. Por favor, ingrese una opción correcta (1, 2 o 3).")