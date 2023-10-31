personaje1 = {}

nombre_del_personaje = input("ingrese el nombre de su personaje: \npara continuar presiona enter")
print([nombre_del_personaje])
categoria = int(input("ingrese la categoria de su personaje: 1|guerrero, 2|cazador, 3|arquero \n presiona enter para continuar"))
print(str(nombre_del_personaje + str(categoria)))
nivel = print("está al nivel: 1")
print(categoria + int("nivel"))
habilidad_principal = int(input("1|+30% de sprinteo   2|+40% combate cuerpo a cuerpo   3|vision nocturna"))
print(nivel + habilidad_principal)