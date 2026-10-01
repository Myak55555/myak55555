P = float(input("Введите значение: "))
d = 10.0
S = 10.0
K = 1
while S <= 200:
    d *= 1 + P / 100
    S += d
    K += 1
print(K, S)