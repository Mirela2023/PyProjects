# 7. Verifică dacă un număr este prim
# Exemplu:
# n = 7 → Output: True
# n = 8 → Output: False
# Un număr prim este un număr natural mai mare decât 1, care are exact doi divizori pozitivi: 1 și el însuși.
# Dacă n are vreun divizor în afară de 1 și n, acel divizor va apărea până la sqrt(n) - radical din n.
# Dacă nu găsim niciun divizor în acel interval, atunci n este prim.

import math

n = int(input("Introduceți n: "))

if n <= 1:
    raspuns = False  # 0 si 1 nu sunt numere prime
else:
    raspuns = True
    for i in range(2, int(math.sqrt(n)) + 1):  # caut divizorii pana la sqrt(n) inclusiv
        if n % i == 0:
            raspuns = False
            break

if raspuns:
    print(f"{raspuns} - {n} este prim")
else:
    print(f"{raspuns} - {n} nu este prim")
