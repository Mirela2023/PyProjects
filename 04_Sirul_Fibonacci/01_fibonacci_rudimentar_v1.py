# 1. Metoda rudimentară
# Folosește doar variabile, condiții și o buclă pentru a obține rezultatul.
# Programul trebuie să pornească de la F(0) = 0 și F(1) = 1 și să continue până la F(n),
# unde n este o valoare dată în cod.

n = int(input("Introduceți n pentru a calcula F(n) din șirul lui Fibonacci: "))

F0 = 0
F1 = 1
sir = [F0] + [F1]

for i in range(1,n):
    sir += [sir[i-1] + sir[i]]

print("Șirul lui Fibonacci pentru n =", n, "este:\n", sir)
print("F(", n, ") =", sir[len(sir)-1])
