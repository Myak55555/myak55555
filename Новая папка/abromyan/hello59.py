N = int(input("Введите значение: "))
r = 0
while N > 0:
    r = r * 10 + N % 10
    N //= 10
print(r)