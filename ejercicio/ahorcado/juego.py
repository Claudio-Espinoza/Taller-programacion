# Crear una lista de palabras
palabra = ""
letras_encontradas = []
contador_intentos = 0
INTENTOS_MAXIMOS = 5
PUNTAJE = 10
puntaje_actual = 0


def adivinar_letra():
    return input("Ingresa una palabra: ")


def convertir_lista(letras_encontradas):
    for indice in range(len(palabra)):
        letras_encontradas.append("_")


def agregar_letra_acertada(letra):
    for numero, indice in enumerate(palabra):
        if indice == letra:
            if "_" in letras_encontradas:
                letras_encontradas[numero] = indice
    print(letras_encontradas)


def verificar_letra_encontrada(letra):
    global contador_intentos, puntaje_actual
    if letra in letras_encontradas:
        contador_intentos += 1
        print(f"\nYa has usado esa palabra, Llevas {contador_intentos} intentos")
        return False
    else:
        puntaje_actual += PUNTAJE
        print(f"\nHaz adivinado la palabra. Tu puntaje es {puntaje_actual}")
        agregar_letra_acertada(letra)
        return True


def buscar_letra_en_palabra(letra, palabra):
    global contador_intentos
    if letra in palabra:
        verificar_letra_encontrada(letra)
        return True
    else:
        contador_intentos += 1
        print(f"\nTe haz equivocado de palabra, tienes {contador_intentos}")
        return False


# Ejecución/Llamado de las funciones --------------------------------------------------------------------------------#

while True:
    palabra = input("Ingresar palabra a buscar: ")
    convertir_lista(letras_encontradas)

    while contador_intentos <= INTENTOS_MAXIMOS:
        letra = adivinar_letra()
        buscar_letra_en_palabra(letra, palabra)

        if letras_encontradas == list(palabra):
            print("Haz ganado")
            break

    condicion = input("\nIngrese 2 para salir, de lo contrario continuara:")
    if condicion == "2":
        break

