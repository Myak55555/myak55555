N = int(input("Введите значение: "))
f = False
while N > 0:
    if N % 10 == 2:
        f = True 
        break
    N //= 10
print(f) 