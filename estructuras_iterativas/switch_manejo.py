a = 8
#El match es una estructura de if con su determinada jerarquia pero simplificado en aplicacion

match a:
    case 1:
        print("La variable es 1")

    case 2:
        print("La variable es 2")

    case 3:
        print("La variable es 3")

    case _:
        print("No es")
