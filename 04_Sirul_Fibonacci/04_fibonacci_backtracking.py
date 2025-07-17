# Backtracking

def fibo_backtracking(n, index, sir):
    if index > n:
        return
    if index == 0:
        sir.append(0)  # F(0)
    elif index == 1:
        sir.append(1)  # F(1)
    else:
        sir.append(sir[index - 1] + sir[index - 2])  # F(index)
    fibo_backtracking(n, index + 1, sir)

n = int(input("Introduceți n pentru a calcula F(n) din șirul lui Fibonacci: "))
sir = []
fibo_backtracking(n, 0, sir)

print(f"Sirul lui Fibonacci pt n = {n}: {sir}")
print(f"F({n}) = {sir[n]}")
