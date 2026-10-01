A = int(input("Введите значение: "))
B = int(input("Введите значение: "))
if A >= B:
    print("Error")
else:
    N= 0 
    for i in range(B - 1, A, -1):
        print(i)
        N += 1
print(N)