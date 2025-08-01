# 11. Transformă secunde în ore:minute:secunde
# Exemplu: input = 3661 → Output: 1:1:1

input_secunde = int(input("Introduceti numarul de secunde: "))

total_min = input_secunde // 60      # 3661 // 60 = 61
ore = total_min // 60                # 61 // 60 = 1
minute = total_min - ore * 60        # 61 - 1*60 = 1
secunde_ramase = input_secunde - (ore * 60 + minute) * 60    # 3661 - (1 * 60 + 1) * 60 = 3661 - 3660 = 1

print(f'{ore}:{minute}:{secunde_ramase}')  # 1:1:1




