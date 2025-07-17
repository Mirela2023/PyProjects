# 3. Cu bibliotecă Python • functools.lru_cache aplicat peste funcția recursivă

import functools
lru_cache = functools.lru_cache

@lru_cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

n = int(input("Introduceți n pentru a calcula F(n) din șirul lui Fibonacci: "))
sir=[]
for i in range(n+1):
    sir.append(fibonacci(i))

print(f"Sirul lui Fibonacci pt n = {n}: {sir}")
print(f"F({n}) = {fibonacci(n)}")
