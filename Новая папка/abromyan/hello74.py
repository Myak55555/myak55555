N = int(input ("Введите значение: "))
s = 0.0
p = 1.0
for i in range(N):
    x = float (input())
    s += x
    p *= x
print("Сумма =", s)
print("Произв =", p)