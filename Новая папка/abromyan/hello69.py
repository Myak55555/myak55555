eps = float(input("Введите значение: "))
A1 = 1.0
A2 = 2.0
K = 2
while abs(A2 - A1) >= eps:
    A1, A2 = A2, (A1 + 2 * A2) / 3
    K += 1
print(K, A1, A2)