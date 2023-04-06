# If simple
if True:
    print("Se cumple la condicion")

# If ejecucion multiple (En una linea)
if True:
    print("Es > 5")
    print("Dentro del if")

# If con jerarquia
variable_1, variable_2 = 1, 2

if variable_1 > 2:
    print("Primera opcion")
elif variable_1 == variable_2:
    print("Segunda opcion")
elif variable_1 == variable_2:
    print("Tercera opcion")
else:
    print("Opcion de excepcion")

# Al tener muchas condiciones
if variable_1 == variable_2 \
        and variable_2 < variable_1 < variable_2 == 4:
    print("Validacion")
