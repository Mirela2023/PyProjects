'''
10. Afișează toți divizorii unui număr `n`
Exemplu: n = 12 → Output: 1 2 3 4 6 12
'''

n = int(input("Introduceti n = "))
sir =''
for i in range(1,n+1):
    if n%i == 0:
        sir += str(i)+' '
print(f'Divizorii lui {n} sunt: {sir}')
