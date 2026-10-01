N = (int(input("Введите значение: ")))
X = float(input("Введите значеие: "))
s = t
t = X
for i in range(1, N +1):
    t *= -X * X / ((2 * k - 1 ) * (2 * k * (2 * k + 1))) 
    s += t
print(s)