# numeros primos

""""
1ro rango de numeros
2do si el numero es multiplo de 2,3,5
"""""


def eximir_primos_base(a):
    return a == 2 or a == 3 or a == 5


def evaluar_primos(a):
    return a % 3 == 0 or a % 5 == 0 or a % 2 == 0


def evaluar_excepción_uno(c):
    return c == 1


for a in range(1, 101):
    if evaluar_excepción_uno(a):
        print(f"{a} no es primo")
    elif eximir_primos_base(a):  # eximir condiciones;
        print(f"{a} es primo")

    else:
        if evaluar_primos(a):  # evaluar primos
            print(f"{a} no es primo")
        else:
            print(f"{a} es primo")
