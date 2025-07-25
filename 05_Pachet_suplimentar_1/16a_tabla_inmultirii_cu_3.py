# 16. Afișează tabla înmulțirii cu `n`
# Exemplu:
# n = 3 → Output: 3 6 9 12 15 18 21 24 27 30

n = int(input("Introduceti n = "))

tabla_inmultirii = []

for i in range(1,11):
    tabla_inmultirii.append(i*n)

print(f'Tabla inmultirii cu {n} - primele 10 rezultate:')
print(f'- lista: {tabla_inmultirii}')
print(f'- string: {' '.join(str(i) for i in tabla_inmultirii)}')
