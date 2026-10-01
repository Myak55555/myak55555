eps = float(input("Введите значение: "))
A_p = 2.0
A = 2 + 1 / A_p
K = 2
while abs(A - A_p) >= eps:
    A_p, A = A, 2 + 1 / A
    K += 1
print(K, A_p, A)