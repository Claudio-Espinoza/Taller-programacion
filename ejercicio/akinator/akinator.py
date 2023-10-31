print("Hola, bienvenido a akinator\n Responde las preguntas y adivinare que medio de transporte ocupas:")

respuesta = input("Akinator: ¿El transporte es terrestre o aéreo\n1 - Terrestre\n 2 - Aéreo")

if respuesta == "1":
    respuesta = input("Akinator: ¿El transporte cuantas ruedas tiene\n1 - Tiene 2 ruedas\n2 - Tiene 4 ruedas")

    if respuesta == "1":
        respuesta = input("Akinator: ¿El transporte cuenta con un motor\n1 - Si\n2 - No")

        if respuesta == "si":
            print("Akinator: Es una moto")
        elif respuesta == "no":
            print("Akinator: Es una bicicleta")
        else:
            print("Esa opción no es valida")

    elif respuesta == "2":
        print("Akinator: Es un auto")
    else:
        print("Esa opción no es valida")

elif respuesta == "2":
    print("Akinator: Es un avion")
else:
    print("Esa opción no es valida")
