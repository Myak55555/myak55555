P = float(input("Введите цену 1кг: "))
for i in range(6, 11):
    W = i / 5
    C = P * W
    print(f"{W} кг - {C}")