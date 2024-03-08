n = int(input("Ingrese un numero entero positivo: "))

if n <= 0:

    print("Vuelva a ingresar un numero entero positivo")

else:

    suma = n*(n+1)//2

print("La suma de los primeros N numeros enteros positivos de" ,n,"son",suma)