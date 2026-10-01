N = (int(input("Введите значение: ")))
X = float(input("Введите значеие: "))
s = 1.0
t = 1.0
for i in range(1, N +1):
    t *= -(2 * i - 3) * X / (2 * i) 
    s += t
print(s)