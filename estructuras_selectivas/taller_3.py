numero_1 = float(input("1. Ingrese un numero: "))
numero_2 = float(input("2. Ingrese un numero: "))
numero_3 = float(input("3. Ingrese un numero: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("El numero " + str(numero_1) + " es mayor")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("El numero " + str(numero_2) + " es mayor")
elif numero_3 > numero_2 and numero_3 > numero_1:
    print("El numero " + str(numero_3) + " es mayor")
else:
    print("Ningun numero es mayor a otro")

print("El promedio es: ", (numero_1 + numero_2 + numero_3)/3)
