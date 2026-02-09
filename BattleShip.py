import random

#  las posiciones actuales  del barcos
barco1 = [1, 1]
barco2 = [3, 4]
barco3 = [5, 5]
flota = [barco1, barco2, barco3]

print("Bienvenido a Batalla Naval")
print("Encuentra los 3 barcos (Rango: 1 a 5)")

# iteración del bucle
while len(flota) > 0:
    intento_fila = int(input("Escribe Fila (1-5): "))
    intento_col = int(input("Escribe Columna (1-5): "))

#fuera del grid
    if intento_fila < 1 or intento_fila > 5 or intento_col < 1 or intento_col > 5:
        print("¡ERROR! Esas coordenadas están fuera del mapa (1-5).")
        continue

    # Creamos una lista con el intento del jugador
    intento = [intento_fila, intento_col]

    # 3. results
    if intento in flota:
        print("Muy Bien! Has hundido un barco.")
        flota.remove(intento)
    else:
        print("¡AGUA! Intenta de nuevo.")

    print(f"Barcos presentos: {len(flota)}")

print("Felicidades, Has ganado!")