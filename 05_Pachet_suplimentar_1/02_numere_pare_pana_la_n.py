# 2. Afișează toate numerele pare până la `n`
# Exemplu: n = 10 → Output: 2 4 6 8 10

n = int(input("Introduceti n: "))
nr_pare = []

for i in range (2,n+1):
    if i % 2 == 0:
        nr_pare.append(i)

print(f"Numerele pare pana la {n} sunt: {nr_pare}")
