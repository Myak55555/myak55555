A = int(input("Введите значение: "))
B = int(input("Введите значение: "))
while B != 0:
    A, B = B, A % B
print(A)