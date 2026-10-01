N = (int(input("Введите значение: ")))
f= 1
s = 0
for i in range(1, N +1):
    f *= i 
    s += f
print(s)