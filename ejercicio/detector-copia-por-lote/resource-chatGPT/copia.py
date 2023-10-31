import string

# |1. Se definen las variables|----------------------------------------------------------------------------------#
ALFABETO_MAYUSCULA = list(string.ascii_uppercase)
CARACTER_ESPECIAL = {'?', '@', '='}
NUMEROS = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

condicion_validadora = False


# |2. Se definen las funciones|----------------------------------------------------------------------------------#

def buscar_elementos(password_local, comparador):
    contador = 0
    for i in password_local:
        for j in comparador:
            if i == j:
                contador += 1
    return contador


def validador_password(password_local):
    if 8 <= len(password_local) <= 16 \
            and buscar_elementos(list(password_local), CARACTER_ESPECIAL) >= 1 \
            and buscar_elementos(list(password_local), ALFABETO_MAYUSCULA) >= 1 \
            and buscar_elementos(list(password_local), NUMEROS) >= 2:
        return True
    else:
        return False


# |3. Ejecutamos|------------------------------------------------------------------------------------------------#

while not condicion_validadora:
    print("Ingrese la contraseña: ")
    password = input()

    condicion_validadora = validador_password(password)
    print("\nAcceso: ", condicion_validadora)

    if not validador_password(password):
        print("Reintente\n")
