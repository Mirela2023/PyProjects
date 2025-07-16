# 3. Cu sympy.fibonacci(n) din biblioteca SymPy

import sympy
fibo = sympy.fibonacci

n = int(input("Introduceți n pentru a calcula F(n) din șirul lui Fibonacci: "))
sir=[]
for i in range(n+1):
    sir.append(fibo(i))

print(f"Sirul lui Fibonacci pt n = {n}: {sir}")
print(f"F({n}) = {fibo(n)}")