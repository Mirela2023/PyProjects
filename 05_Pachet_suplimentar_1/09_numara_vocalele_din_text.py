# 9. Numără vocalele dintr-un text
# Exemplu:
# text = "informatica" → Output: 5

text = input("Introduceti textul: ")
vocale = ['a', 'ă', 'â', 'e', 'i', 'o', 'u']

lista = list(text)
nr_vocale = 0

for i in range(0,len(lista)):
    for j in range(0,len(vocale)):
        if lista[i] == vocale[j] or lista[i].upper() == vocale[j].upper():
            nr_vocale += 1

print(f'"{text}" contine {nr_vocale} vocale.')
