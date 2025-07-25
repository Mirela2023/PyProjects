'''
5. Verifică dacă un cuvânt este palindrom
Exemplu:
text = "ana" → Output: True
text = "python" → Output: False

Alte exemple de palindroame:
radar, cojoc, level, rotor, madam, civic, kayak, refer, deified, reviver
'''

cuvant = input("Introduceti cuvantul: ")

listaCuv = list(cuvant)  # pun literele cuvantului intr-o lista
listaInv = listaCuv[::-1]  # listaCuv inversata

# compar listele intre ele:
# daca literele de pe aceeasi pozitie sunt egale intre ele, atunci e True;
# altfel, e False
for i in range(len(listaCuv)):
    if listaCuv[i] == listaInv[i]:
        raspuns = True
    else:
        raspuns = False

print(f'Este {cuvant.upper()} palindrom? {raspuns}')
