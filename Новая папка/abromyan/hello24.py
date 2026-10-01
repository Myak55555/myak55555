N = (int(input("Введите значение: ")))
X = float(input("Введите значеие: "))
s = 1.0
t = 1.0
for i in range(1, N +1):
    t *= -X * X / ((2 * k - 1) * (2 * k )) 
    s += t
print(s)