# 1. Suma primelor `n` numere naturale
# Exemplu: n = 5 → Output: 15 (1 + 2 + 3 + 4 + 5)

n = int(input("Introduceti n: "))
suma = 0
lista = []
for i in range (1,n+1):
    lista.append(i)
    suma += i
print(f"Suma primelor {n} numere naturale {lista} este {suma}")
