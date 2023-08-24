opcion_seleccionada = int(input("Bienvenido a la calculadora\nQue desea hacer:"
                                "\n1 - Sumar\n2 - Restar\n3 - Dividir\n4 - Multiplicar\n5 - Potenciar\n6 - Modulo"
                                "\nIngrese una opcion:"))

numero_1 = int(input("Ingrese el primer numero:"))
numero_2 = int(input("Ingrese el segundo numero:"))

if opcion_seleccionada == 1:
    print(f"El resultado es {numero_1 + numero_2}: ")

elif opcion_seleccionada == 2:
    print(f"El resultado es {numero_1 - numero_2}: ")

elif opcion_seleccionada == 3:
    print(f"El resultado es {numero_1 / numero_2}: ")

elif opcion_seleccionada == 4:
    print(f"El resultado es {numero_1 * numero_2}: ")

elif opcion_seleccionada == 5:
    print(f"El resultado es {numero_1 ** numero_2}: ")

elif opcion_seleccionada == 6:
    print(f"El resultado es {numero_1 % numero_2}: ")

else:
    print("Opción no valida")
