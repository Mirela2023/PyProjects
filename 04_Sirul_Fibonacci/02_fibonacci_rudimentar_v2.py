# 1. Metoda rudimentară
# Folosește doar variabile, condiții și o buclă pentru a obține rezultatul.
# Programul trebuie să pornească de la F(0) = 0 și F(1) = 1 și să continue până la F(n),
# unde n este o valoare dată în cod.

n = int(input("Introduceți n pentru a calcula F(n) din șirul lui Fibonacci: "))

F0 = 0
F1 = 1

for i in range(1, n):
    var_temp= F0
    F0 = F1
    F1 = F1 + var_temp

print("F(", n, ") =", F1)
