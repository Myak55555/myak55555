N = (int(input("Введите значение: ")))
K = (int(input("Введите значение: ")))
s = 0.0
for i in range (1, N + 1):
    s += i ** K
print(s)