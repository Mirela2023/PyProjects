# 7. Verifică dacă un număr este prim
# Exemplu:
# n = 7 → Output: True
# n = 8 → Output: False
# Un număr prim este un număr natural mai mare decât 1, care are exact doi divizori pozitivi: 1 și el însuși.

n = int(input("Introduceti n: "))
lista = []
for i in range(1,n+1):
    if n % i == 0:
        lista.append(i)   # lista cu divizorii lui n

raspuns = len(lista) == 2  # True daca lista are 2 divizori (1 si n), False in rest

if raspuns:
    print(f"{raspuns} - {n} este prim")
else:
    print(f"{raspuns} - {n} nu este prim")
print(f"Divizorii lui {n} sunt: {lista}")