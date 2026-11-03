import random

print("=" * 50)
print("     SIMULACION DE LANZAMIENTO DE UN DADO")
print("=" * 50)

n = int(input("¿Cuantos lanzamientos deseas realizar?: "))

frecuencias = [0] * 6

for i in range(n):
    dado = random.randint(1, 6)
    frecuencias[dado - 1] += 1

print("\nRESULTADOS DE LA SIMULACION")
print("-" * 50)
print(f"{'Cara':<10}{'Frecuencia':<15}{'Probabilidad'}")
print("-" * 50)

for cara in range(1, 7):
    frecuencia = frecuencias[cara - 1]
    probabilidad = frecuencia / n if n > 0 else 0

    print(f"{cara:<10}{frecuencia:<15}{probabilidad:.4f}")

print("-" * 50)
print(f"Total de lanzamientos: {n}")
print(f"Suma de frecuencias: {sum(frecuencias)}")
print("=" * 50)
