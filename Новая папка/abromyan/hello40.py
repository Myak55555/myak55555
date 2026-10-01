A = (int(input("Введите значение: ")))
B = (int(input("Введите значение: ")))
for i in range (A, B + 1):
    print((str(i) + " ") * ( i - A + 1), end = " ")
print()