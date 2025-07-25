# 15. Numără câte cuvinte are o propoziție
# Exemplu:
# text = "Ana are mere multe" → Output: 4

text = input("Introduceti propozitia: ")
lista_cuvinte = text.split()
print(f'Propozitia are {len(lista_cuvinte)} cuvinte.')
