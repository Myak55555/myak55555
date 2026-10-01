N = int(input ("Введите значение: "))
s = 0
for i in range(N):
    x = float(input())
    r = round(x)
    print(r)
    s += r
print("Сумма =", s)