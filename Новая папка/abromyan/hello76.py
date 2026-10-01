N = int(input ("Введите значение: "))
p = 1.0
for i in range(N):
    x = float (input())
    f = x - int(x)
    print(f)
    p *= f
print("Произв =", s)