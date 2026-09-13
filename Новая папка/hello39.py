A = float(input("Введите значение: "))
B = float(input("Введите значение: "))
C = float(input("Введите значение: "))
D = B**2 - 4 * A * C
if D > 0:
    x1 = (-B + D**0.5) / (2*A)
    x2 = (-B - D**0.5) / (2*A)
    print("Решение = 0")
elif D == 0:
    x = -B / (2*A)
    print("Решение = 0")
else:
    print("нет решений")
