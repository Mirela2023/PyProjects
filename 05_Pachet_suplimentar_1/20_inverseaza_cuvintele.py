'''
20. Scrie un program care inversează cuvintele dintr-o propoziție
Exemplu:
text = "Ana are mere" → Output: "mere are Ana"
'''

text = input("Introduceti propozitia: ")

lista_cuvinte = text.split()  # pun cuvintele intr-o lista

lista_cuvinte.reverse()  # inversez lista

prop_inversata = ' '.join(str(cuvant) for cuvant in lista_cuvinte)  # transform lista inversata in string

print(prop_inversata)
