N = int(input ("Введите значение: "))
K = 0
for i in range(N):
    x = int(input())
    if x % 2 == 0:
    print(x)
    K += 1
print("Колво =", K)