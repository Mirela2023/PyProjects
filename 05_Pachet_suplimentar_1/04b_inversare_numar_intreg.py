'''
4. Inversarea unui număr întreg
Exemplu: n = 1234 → Output: 4321
'''

n = int(input("Introduceti n: "))

n_invers = int(str(n)[::-1])

print(f"Inversul lui {n} este {n_invers}")
