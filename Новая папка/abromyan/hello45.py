N = int(input("Введите значение: "))
K = 0
while N > 1:
    N //= 2
    K += 1
print(K)