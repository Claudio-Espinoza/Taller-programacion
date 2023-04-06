#While
x = 5

while x > 0:
    x -= 1
    print(x)  #4,3,2,1,0
else:
    print("El bucle ha finalizado")

#Do while
x = 5
while True:
    x -= 1
    print(x)  #4, 3, 2, 1, 0

    if x == 0:
        break



# Permutación a generar
i = 0
j = 0
while i < 3:
    while j < 3:
        print(i, j)
        j += 1
    i += 1
    j = 0

#Es equivalente a usar for anidados

for i in range(4):
    for j in range(4):
        print(i, j)
