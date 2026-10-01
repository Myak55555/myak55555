N = (int(input("Введите значение: ")))
f1 = 1
f2 = 2
print( f1 )
print( f2 )
for i in range (3, N + 1):
    f3 = (f1 + 2 * f2 ) / 3
    print(f3)
    f1,f2 = f2, f3