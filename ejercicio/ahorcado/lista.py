""""""
s = "Messi"
for h, i in enumerate(s):
    print(f"{i} es: {h}")
""""""
"""""
Diseña un sistema de gestión de biblioteca. En este programa deberás considerar que el 
usuario podrá elegir entre prestar y pedir libros. Para esto se le debe dar la opción al 
usuario de ver todo el catálogo de libros, buscar un libro en específico y seleccionar un libro.
En el caso de pedir un libro, debe quedar un registro de tal acción y que se genere una boleta 
donde se muestre el nombre del usuario, libro pedido y los días de prestamo.

condiciones:
Se debe hacer uso de listas y/o Strings
Se debe hacer un uso apropiado de los contenidos revisados en el curso hasta el momento (Estructura de control / Funciones).
Escriba un análisis del problema o una descripción de lo que hace su código
Declare cuáles son los inputs y outputs.
"""""
# 1ro crear la biblioteca
# 1ro crear catalogo
# 1ro existencia del libro
# 1ro si presta un libro, dejar registro y dar boleta
# 1ro
# 1ro

catalogo = ["pinocho", "el viejo y el mar", "sombras oscuras"]
print(catalogo)


def buscar_libro():
    a = input("ingrese su libro a buscar: ")
    if a in catalogo:
        print("su libro esta en la biblioteca")


def pedir_libro():
    a = input("ingrese su libro a pedir: ")
    if a in catalogo:
        catalogo.remove(a)
        print(catalogo)
        return a


def prestar_libro():
    b = input("ingrese su libro a ingresar")
    catalogo.append(b)


if __name__ == '__main__':
    print("Bienvenido a Sufro")
    eleccion_usuario = int(input("si quieres buscar un libro press: 1"
                                 "\nsi quieres pedir un libro press: 2"
                                 "\nsi quieres prestar un libro press: 3\nResultado: "))
    if   eleccion_usuario == 1:
        buscar_libro()
    elif eleccion_usuario == 2:
        pedir_libro()
    elif eleccion_usuario == 3:
        prestar_libro()
    else:
        print("no existe la alternativa")
