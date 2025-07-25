# 16. Afișează tabla înmulțirii cu `n`
# Exemplu:
# n = 3 → Output: 3 6 9 12 15 18 21 24 27 30

n = int(input("Introduceti n = "))
nr_afisari = int(input("Numar de afisari = "))

tabla_inmultirii = []

for i in range(1,nr_afisari+1):
    tabla_inmultirii.append(i*n)

print(f'Tabla inmultirii cu {n} - primele {nr_afisari} rezultate:')
print(f'- lista: {tabla_inmultirii}')
print(f'- string: {' '.join(str(i) for i in tabla_inmultirii)}')
