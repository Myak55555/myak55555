P = float(input("Введите цену 1кг конфет: "))
for i in range(1, 11):
    W = i / 10
    C = P * W
    print(f"Стоимость {W} кг: {C}")