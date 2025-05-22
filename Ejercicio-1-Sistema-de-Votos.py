# Crear un programa que simule un sistema de gestión de votos

localidades = [['' for i in range(3)] for j in range(5)]

i = 0
while i != 5:
    print(f"--LOCALIDAD {i+1}--")
    for j in range(3):
        localidades[i][j] = int(input(f"Ingrese los votos del partido {j+1} (max:300): "))
    if (localidades[i][0] + localidades[i][1] + localidades[i][2]) <= 300:
        i += 1
    else:
        print("La cantidad de votantes ingresados es mayor a 300. Por favor, respete la condición")

for i in localidades:
    print(i)