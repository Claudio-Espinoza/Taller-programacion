#For manipulando objetos
for i in "Python":
    print(i)

# Salida:
# P
# y
# t
# h
# o
# n

#For con "range"
#Esta estructura es la mas arcaica y semejante a la de un for i:
#for (i = 0 ; i < n ; i++)
#incio, limite, contador

for i in range(0, 5, 2):
    print(i)

    #Salida
    #2
    #4

#Funcionalidad extra
#range(inicio, fin, salto) Como se ve se mantiene la estructura del for i
#for (i = 0 ; i < n ; i++) en este caso quedaria asi #for (i = 0 ; i < n ; i+ = 2)
for i in range(5, 20, 2):
    print(i)
    #5,7,9,11,13,15,17,19

lista = ["A", "B", "C"]

for indice, l in enumerate(lista):
    print(indice, l)

# Salida:
# 0 A
# 1 B
# 2 C

#Iterador
lista = [5, 6, 3, 2]
it = iter(lista)
print(next(it))
print(next(it))
# Salida:
# 5
# 6

#Zip
numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)

for n, e, i, f in zip(numeros, espanol, ingles, frances):
    print(n, e, i, f)

# 1 Uno One Un
# 2 Dos Two Deux
