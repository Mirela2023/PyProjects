'''
4. Inversarea unui număr întreg
Exemplu: n = 1234 → Output: 4321
'''

n = int(input("Introduceti n: "))  # 1234 - nr. intreg

n_string_initial = str(n)         # 1234 - string
n_lista = list(n_string_initial)  # ['1', '2', '3', '4']  1234 - lista
n_lista.reverse()                 # ['4', '3', '2', '1'] lista inversata

n_string_final = ''.join(str(i) for i in n_lista)  # 4321 - string

n_inversat = int(n_string_final)  # 4321 - nr. intreg

print(f'{n} inversat este {n_inversat}')
