'''
13. Afișează un șir descrescător de la `n` la 1
Exemplu: n = 5 → Output: 5 4 3 2 1
'''
n = int(input("Introduceti n = "))

sir=[]
for i in range(1,n+1):
    sir.append(i)
sir.reverse()

sir_string = ' '.join(str(i) for i in sir) # transform sir din lista in string

print(sir_string)
