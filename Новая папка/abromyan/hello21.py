N = (int(input("Введите значение: ")))
f = 1.0
s = 1.0
for i in range(1, N +1):
    f *= i 
    s += 1 / f
print(s)