N = (int(input("Введите значение: ")))
a1, a2, a3 = 1, 2, 3

for i in range (4, N + 1):
    a4 = a3 + a2 - 2 * a1
    print(a4, end = " ")
    a1, a2, a3 = a2, a3, a4
print()