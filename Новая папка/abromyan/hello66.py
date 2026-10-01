N = int(input("Введите значение: "))
f1, f2 = 1, 1
while f2 < N:
    f1, f2 = f2, f1 + f2
f_next = f1 + f2
print(f1, f_next)