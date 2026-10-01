A = float(input("Введите значение: "))
N = int(input("Введите значение: "))
s = 1.0
p = 1.0 
si = -1
for i in range (1, N + 1):
    p *= A
    s += si * p
    si = -si
print(s) 