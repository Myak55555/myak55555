N = int(input("Введите значение: "))
K = 1
while (K + 1) * (K + 1) <= N:
    K += 1
print(K)