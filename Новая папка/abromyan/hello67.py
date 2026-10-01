N = int(input("Введите значение: "))
f1, f2 = 1, 1
K = 2
while f2 < N:
    f1, f2 = f2, f1 + f2
    K += 1
print(K)