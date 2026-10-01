A = int(input("Введите значение: "))
B = int(input("Введите значение: "))
if A >= B:
    print("Error")
else:
    N= 0 
    for i in range(A,B +1):
        print(i)
        N += 1
print(N)