# 12. Află suma cifrelor unui număr
# Exemplu:
# n = 123 → Output: 6

n = int(input("Introduceti n: "))
string = str(n)  # transform n in string
lista = list(string)  # pun cifrele de tip string intr-o lista, ['1', '2', '3']

# fac o lista noua cu cifrele transformate din string in nr. intregi
lista_nr_intregi=[]
for i in range(len(lista)):
    lista_nr_intregi.append(int(lista[i]))

# suma elementelor din lista cifrelor-nr.intregi
suma = 0
for i in range(len(lista_nr_intregi)):
    suma += lista_nr_intregi[i]

print(f'Suma cifrelor numarului {n} este {suma}.')
