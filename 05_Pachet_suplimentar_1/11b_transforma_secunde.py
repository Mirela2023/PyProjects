# 11. Transformă secunde în ore:minute:secunde
# Exemplu: input = 3661 → Output: 1:1:1

# Funcția care transformă secundele în ore:min:sec (format 1:1:1)
def transforma(secunde):
    ore = secunde // 3600             # 3661 // 3600 = 1
    minute = (secunde % 3600) // 60   # (3661 % 3600) // 60 = 61 // 60 = 1
    sec = secunde % 60                # 3661 % 60 = 1
    return f"{ore}:{minute}:{sec}"    # 1:1:1

input_secunde = int(input("Introduceti numarul de secunde: "))
format_nou = transforma(input_secunde)
print(format_nou)
