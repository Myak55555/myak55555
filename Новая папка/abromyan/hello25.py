N = (int(input("Введите значение: ")))
X = float(input("Введите значеие: "))
s = X
t = X
for i in range(2, N +1):
    t *= -X 
    s += t / i
print(s)