N = int(input("Введите значение: "))
p = 1.0
for i in range(1, N + 1):
    p *= (10 *i) / 10
print(p)