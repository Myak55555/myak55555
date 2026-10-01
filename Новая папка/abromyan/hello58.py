N = int(input("Введите значение: "))
c = 0
s = 0
while N > 0:
    s += N % 10
    c += 1
    N //= 10
print(c , S)