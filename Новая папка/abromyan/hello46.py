N = int(input("Введите значение: "))
p = 1.0
while N > 0:
    p *= N
    N -= 2
print(p)