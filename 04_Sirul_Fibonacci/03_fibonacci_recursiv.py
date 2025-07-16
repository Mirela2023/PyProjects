# Sirul lui Fibonacci recursiv

# Functia recursiva care calculeaza elementele din sirul lui Fibonacci
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

n = int(input("Introduceți n pentru a calcula F(n) din șirul lui Fibonacci: "))
sir=[]
for i in range(n+1):
    sir += [fibonacci(i)]

print("Sirul lui Fibonacci pt n =", n, ": ", sir)
print(f"F({n}) = {fibonacci(n)}")
