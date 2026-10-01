N = int(input("Введите значение: "))
s = 0
for i in range(N, 2 * N + 1):
    s += i * i
print(s)