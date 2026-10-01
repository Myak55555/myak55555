P = float(input("Введите значение: "))
S = 1000.0
K = 0
while S <= 1100:
    S *= 1 + P / 100
    K += 1
print(K, S)