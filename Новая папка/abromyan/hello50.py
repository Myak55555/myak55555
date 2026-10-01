N = int(input("Введите значение: "))
K = 0
p = 1
while p * 3 < N:
    p *= 3
    K += 1
print(K)