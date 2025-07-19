# 6. Află cel mai mare din trei numere
# Exemplu: a = 4, b = 9, c = 1 → Output: 9

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a > b:
    if b > c:
        maxim = a
    else:
        if a > c:
            maxim = a
        else:
            maxim = c
else:
    if b > c:
        maxim = b
    else:
        maxim = c

print(f"Cel mai mare numar dintre {a}, {b}, {c} este {maxim}.")