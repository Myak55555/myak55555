A = float(input("Введите значение: "))
B = float(input("Введите значение: "))
C = float(input("Введите значение: "))
c = 0
while A >= C:
    b = B
    while b >= C:
        c += 1
        b -= C
    A -= C
print(c)