N = int(input("Введите значение: "))
K = 0 
s = 0
while s + K + 1 <= N:
    K += 1
    s += K
print(K, s)