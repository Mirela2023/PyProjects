# 3. Calculează factorialul unui număr `n`
# Exemplu: n = 4 → Output: 24 (4*3*2*1)

n = int(input("Introduceti n: "))
factorial = 1

for i in range(1,n+1):
    factorial *= i

print(f"{n}! = {factorial}")