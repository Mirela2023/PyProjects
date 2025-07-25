# 12. Află suma cifrelor unui număr
# Exemplu:
# n = 123 → Output: 6

def calculeaza_suma(n):
    suma = 0
    while n != 0:
        cifra = n % 10 # cifra pastreaza valoarea restului impartirii lui n la 10 (ultima cirfra)
        suma += cifra  # suma se actualizeaza pe masura ce adaug ultima cifra la fiecare pas
        n //= 10       # actualizez n, eliminand ultima cifra prin impartirea intreaga a lui n la 10
    return suma

n = int(input("Introduceti n: "))
suma_cifrelor = calculeaza_suma(n)
print(f'Suma cifrelor numarului {n} este {suma_cifrelor}.')
