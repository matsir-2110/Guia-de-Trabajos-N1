# Crear un programa que simule un sistema de gestión de votos

localidades = [['' for i in range(3)] for j in range(5)]

#Sistema de agregado de votos
i = 0
while i != 5:
    print(f"--LOCALIDAD {i+1}--")
    for j in range(3):
        localidades[i][j] = int(input(f"Ingrese los votos del partido {j+1} (max:300): "))
    if (localidades[i][0] + localidades[i][1] + localidades[i][2]) <= 300:
        i += 1
    else:
        print("La cantidad de votantes ingresados es mayor a 300. Por favor, respete la condición")


#Impresión de Resultados de votos
print("\n")
cont = 1
for i in localidades:
    print(f"--LOCALIDAD {cont}--", i)
    cont += 1

#Ganador
win_1 = 0
win_2 = 0
win_3 = 0

for i in range(5):
    win_1 += localidades[i][0]
    win_2 += localidades[i][1]
    win_3 += localidades[i][2]

if win_1 > win_2 and win_1 > win_3:
    print(f"El partido 1 es el ganador con {win_1} votos")
elif win_2 > win_1 and win_2 > win_3:
    print(f"El partido 2 es el ganador con {win_2} votos")
elif win_3 > win_1 and win_3 > win_2:
    print(f"El partido 3 es el ganador con {win_3} votos")
else:
    print("Hay un empate entre partidos")